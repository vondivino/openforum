from forums.models import Forum

def slug_clean(Object, keyword):
    keyword = keyword.replace(' ', '-').strip('?!.')
    counter = 0
    while True:
        queryset = Object.objects.filter(slug=keyword)
        if queryset:
            if counter == 0:
                keyword = queryset.first().slug + f'-{counter}'
            else:
                letters = list(keyword)
                letters[-1] = str(counter)
                keyword = ''.join(letters)
        else:
            return keyword
        counter += 1
