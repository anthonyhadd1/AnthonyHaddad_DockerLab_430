# C:\videostore\movies\views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Video
from .forms import VideoForm

# LIST
def video_list(request):
    q = request.GET.get('q', '').strip()
    videos = Video.objects.all()
    if q:
        videos = videos.filter(MovieTitle__icontains=q)
    return render(request, 'movies/video_list.html', {"videos": videos, "q": q})

# DETAIL
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'movies/video_detail.html', {"video": video})

# CREATE
def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Video added successfully!")
            return redirect('movies:list')
    else:
        form = VideoForm()
    return render(request, 'movies/video_form.html', {"form": form, "mode": "Create"})

# UPDATE
def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, "Video updated successfully!")
            return redirect('movies:detail', pk=video.pk)
    else:
        form = VideoForm(instance=video)
    return render(request, 'movies/video_form.html', {"form": form, "mode": "Update"})

# DELETE
def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        messages.success(request, "Video deleted.")
        return redirect('movies:list')
    return render(request, 'movies/video_confirm_delete.html', {"video": video})
