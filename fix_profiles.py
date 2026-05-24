from django.contrib.auth.models import User
from repository.models import Profile

print("Checking for users without profiles...")

for user in User.objects.all():
    try:
        profile = user.profile
        print(f"✓ {user.username} already has profile")
    except:
        profile = Profile.objects.create(user=user, is_paid=False)
        print(f"✅ Created profile for {user.username}")

print("Done! All users now have profiles.")