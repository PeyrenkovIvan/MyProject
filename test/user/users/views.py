from django.shortcuts import render, redirect, get_object_or_404
from .models import User , Group , Together
from .forms import UserForm , GroupForm
from django.http import HttpResponse

def index(request):
	
	return render(request, 'users/index.html')

def users(request):

	users = User.objects.order_by('-id')
	groups = Group.objects.order_by('-id')

	context = {
		'users' : users,
		'groups' : groups

	}
	
	return render(request, 'users/users.html', context)

def adduser(request):

	form = None

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			nickname = form.cleaned_data['nickname']
			groups = form.cleaned_data['groups']
			
			user = User(nickname=nickname)
			user.save()

			user.groups.set(groups)

			for group in groups:
				Together.objects.create(user=user , group=group)
			
			return redirect('users')

	else:
		form = UserForm()

	context = {
		'form' : form  
	}
	
	return render(request, 'users/adduser.html', context)

def groups(request):

	groups = Group.objects.all()

	context = {
		'groups' : groups

	}
	
	return render(request, 'users/groups.html' , context)

def addgroup(request):

	if request.method == 'POST':
		form = GroupForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			group = Group(name=name , description=description)
			group.save()

			return redirect('groups')

	else:
		form = GroupForm()

	context = {
		'form' : form

	}
	
	return render(request, 'users/addgroup.html', context)


def edit(request, user_id):

	user = get_object_or_404(User, id=user_id)

	if request.method == 'POST':
		form_data = request.POST
		user.nickname = form_data['nickname']
		user.save()
		return redirect('users')

	context = {
		'user': user

	}


	return render(request, 'users/edit.html', context)


def delete(request, user_id):

	user = get_object_or_404(User, id=user_id)

	if request.method == 'POST':
		user.delete()
		return redirect('users')

	context = {
		'user': user

	}

	return render(request, 'users/delete.html', context)


def edit_group(request, group_id):

	group = get_object_or_404(Group, id=group_id)

	if request.method == 'POST':
		form = GroupForm(request.POST)
		if form.is_valid():
			group.name = form.cleaned_data['name']
			group.description = form.cleaned_data['description']
			group.save()

			return redirect('groups')

	else:
		form = GroupForm()

	context = {
		'form': form

	}


	return render(request, 'users/edit_group.html', context)


def delete_group(request, group_id):

	group = get_object_or_404(Group, id=group_id)

	if request.method == 'POST':
		if group.members.exists():
			error = HttpResponse("Удалить группу невозможно, в ней есть пользователи.")
			return error
		else:
			group.delete()
			return redirect('groups')

	context = {
		'group': group,
		'error': error if 'error' in locals() else None,

	}

	return render(request, 'users/delete_group.html', context)