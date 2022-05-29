# graetkart

თუ საკმარისი პროდუქტები არაა - გადანომრვა რომ არ გამოიტანოს:

{% if products.has_other_pages %}

{{ i.variation_category | capfirst }}: {{ i.variation_value | capfirst }}

{{ form.first_name }}

მეილის გაგზავნის დროს gmail-ზე
Less secure app access   =>  on

თუ გადამისამართება გვინდა იგივე გვერდზე updated მერე: 
*    url = request.META.get('HTTP_REFERER')
*    if request.method == 'POST':
*        try:
*            form = ReviewForm(request.POST, instance=reviews) ინსტანსი უნდა რომ ახალი არ შექმნას.
*            return redirect(url)

#### change password (check password-ის დახმარებით)
*         if new_password == confirm_password:
*            success = user.check_password(current_password)
*            if success:
*                user.set_password(new_password)

##### pip install django-admin-thumbnails

## github security:

* pip install python-decouple
*** (create .env file)
* from decouple import config (in setting file)
* ** SECRET_KEY = config('SECRET_KEY')
** DEBUG = config('DEBUG', default=False, cast=bool)
** EMAIL_HOST = config('EMAIL_HOST', default='localhost')
** EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
