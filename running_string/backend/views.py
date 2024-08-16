from django.shortcuts import render
from django.http import FileResponse
from .forms import VideoForm

from .utils import create_running_string

def create(request):

    form = VideoForm(
        request.POST,
    )
    if form.is_valid():
        form.save()
        name = request.POST['name']
        file = create_running_string(name)
        form.save(commit=False)
        return FileResponse(open(file, 'rb'), as_attachment=True)

    context = {'form':form}
    return render(request, 'index.html', context)
