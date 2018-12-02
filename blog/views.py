from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Peter Smith',
        'title': 'Blog Post 1',
        'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus iste debitis, magni architecto iusto error eius omnis mollitia dolor sequi voluptates quos vero consequatur eligendi sed vel officia eos veniam hic. Eum ea laboriosam quasi eaque non aut enim, sit architecto placeat commodi magnam, delectus reprehenderit odio natus. Dolorem consequatur, temporibus, delectus beatae ullam repudiandae consectetur molestiae rerum unde reprehenderit laborum. Amet explicabo impedit, dolorem at repudiandae dicta non labore excepturi placeat quam ipsum fugiat vel sint accusantium nihil! Dicta ab impedit repudiandae aspernatur laboriosam tempore saepe quae consequatur blanditiis? Libero voluptas minima sint fugiat ipsum sapiente quibusdam reiciendis inventore.',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Mike Donald',
        'title': 'Blog Post 2',
        'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus iste debitis, magni architecto iusto error eius omnis mollitia dolor sequi voluptates quos vero consequatur eligendi sed vel officia eos veniam hic. Eum ea laboriosam quasi eaque non aut enim, sit architecto placeat commodi magnam, delectus reprehenderit odio natus. Dolorem consequatur, temporibus, delectus beatae ullam repudiandae consectetur molestiae rerum unde reprehenderit laborum. Amet explicabo impedit, dolorem at repudiandae dicta non labore excepturi placeat quam ipsum fugiat vel sint accusantium nihil! Dicta ab impedit repudiandae aspernatur laboriosam tempore saepe quae consequatur blanditiis? Libero voluptas minima sint fugiat ipsum sapiente quibusdam reiciendis inventore.',
        'date_posted': 'September 27, 2018'
    }
]

def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})