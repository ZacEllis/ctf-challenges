## Zucced
Password link was generated like this, so...
```
def forgot_password():
    if request.method == 'POST':
        username = request.form.get('username', '')
        recovery = hashlib.md5(username.encode("utf")).hexdigest()
        recovery_addr = request.url_root+"recover/"+username+"/"+recovery
        print (recovery_addr)
        if get_email(username) != None:
            email_reset(recovery_addr, get_email(username))
            return render_template('forgot_password.html', message="Email Sent!")

```

So to get the flag, go to <url>/admin/md5(admin)

