from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404
#from django.core.urlresolvers import reverse 在django2中需要用下面的import
from django.urls import reverse
# 添加装饰器，只允许登陆的用户请求
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.
def index(request):
    ''' 学习笔记的主页 '''
    return render(request,"django1_prj_app1/index.html")

@login_required#限制访问
def topics(request):
    """显示所有的主题"""
    # topics = Topic.objects.order_by("date_added")
    # 下面的代码表示为主题所属的用户，展现所有的主题
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')#这里一开始打错了，打成了data_added了，因此出错
    # 一个上下文字典，传递给模板
    context = {'topics': topics}
    return render(request, "django1_prj_app1/topics.html", context)
    #一开始把上面的topics.html打成hmnl了，发生了错误

@login_required
def topic(request,topic_id):
    ''' 显示单个主题及所有的条目 '''
    topic = get_object_or_404(Topic, id=topic_id)
    # topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    if topic.owner !=request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'django1_prj_app1/topic.html', context)

@login_required
def new_topic(request):
    """ 添加新主题 """
    if request.method != 'POST':
        #未提交的数据，创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('django1_prj_app1:topics'))
    context = {'form':form}
    return render(request,'django1_prj_app1/new_topic.html',context)

@login_required
def new_entry(request, topic_id):
    ''' 在特定的主题中添加新条目 '''
    topic = Topic.objects.get(id=topic_id)

    if request.method !='POST':
        #未提交数据，创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # 添加新主题时关联到特定用户
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            # 该类将用户重定向到网页topics，函数reverse()根据指定的URL模型确定URL
            return HttpResponseRedirect(reverse('django1_prj_app1:topic',args=[topic_id]))
    
    context = {'topic':topic, 'form':form}
    return render(request,'django1_prj_app1/new_entry.html',context)

@login_required  
def edit_entry(request, entry_id):
    ''' 编辑既有条目 '''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method !='POST':
        #初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('django1_prj_app1:topic',args=[topic.id]))#注意，这里是topic.id,不要写错，写成topic_id
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'django1_prj_app1/edit_entry.html',context)