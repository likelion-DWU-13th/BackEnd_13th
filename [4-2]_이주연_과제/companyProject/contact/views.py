from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactMessage, Comment
from .forms import ContactModelForm, CommentForm
from django.core.paginator import Paginator

# 폼 
def submitContact(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = ContactModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactModelForm()
        return render(request, 'contact.html', {'form':form } )

# 연락 리스트
def contact_list(request):
    contacts = ContactMessage.objects.all().order_by('-created_at')
    myPaginator = Paginator(contacts, 7)
    pageNum = request.GET.get('page')
    contacts = myPaginator.get_page(pageNum)
    return render(request, "contact_list.html", {"contacts":contacts})

# contact 상세 페이지
def contact_detail(request, id):
    contact = get_object_or_404(ContactMessage, pk=id)
    comment_form = CommentForm()
    context = {
        'contact':contact,
        'comment_form':comment_form
    }
    return render(request, "contact_detail.html", context)

# contact 수정
def contact_edit(request, id):
    contact = get_object_or_404(ContactMessage, pk=id)
    
    if request.method == 'POST'or request.method == 'FILES':
        form = ContactModelForm(request.POST, request.FILES ,instance=contact)
        if form.is_valid():
            form.save()  
            return redirect('contact_list')  
    else:
        form = ContactModelForm(instance=contact)
        return render(request, 'contact.html', {'form': form, 'id': id})
    
# contact 삭제
def contact_delete(request, id):
    contact = ContactMessage.objects.get(pk=id)
    contact.delete()
    return redirect('contact_list')

#댓글 생성
def create_comment(request, contact_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(ContactMessage, pk=contact_id)
        finished_form.save()
    return redirect('contact_detail', contact_id)

#댓글 수정
def update_comment(request, contact_id, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        updated_form = CommentForm(request.POST, instance=comment)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('contact_detail',contact_id)
    else:
        comment_form =CommentForm(instance=comment)
        context = {'comment_form':comment_form}
        return render(request, 'comment_update.html', context)

#댓글 삭제
def delete_comment(request, contact_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('contact_detail', contact_id)