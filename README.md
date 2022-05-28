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

#### check password
*         if new_password == confirm_password:
*            success = user.check_password(current_password)
