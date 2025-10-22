# File: mini_insta/models.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/26/2025
# Description: Defines the Profile model.

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """Encapsulate the data of a Profile by a user"""

    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.TextField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"username: {self.username}, display name: {self.display_name}"

    def get_all_posts(self):
        """Return a QuerySet of Posts by this Profile."""

        posts = Post.objects.filter(profile=self).order_by(
            "-timestamp"
        )  # the negative before timestamp shows descending
        return posts

    def get_absolute_url(self):
        """Return a URL to display the updated Profile."""
        return reverse("show_profile", kwargs={"pk": self.pk})

    def get_followers(self):
        """Return a list of Profiles who are followers of this Profile."""
        followers = Follow.objects.filter(profile=self)
        followerProfiles = []

        for follower in followers:
            followerProfiles.append(follower.follower_profile)

        return followerProfiles

    def get_num_followers(self):
        """Return the count of Followers."""

        followers = self.get_followers()
        count = 0
        for _ in followers:
            count += 1

        return count

    def get_following(self):
        """Return the Profiles followed by this Profile."""
        following = Follow.objects.filter(follower_profile=self)
        followingProfiles = []

        for follow in following:
            followingProfiles.append(follow.profile)

        return followingProfiles

    def get_num_following(self):
        """Return the count of Following."""

        following = self.get_following()
        count = 0
        for _ in following:
            count += 1

        return count

    def get_post_feed(self):
        """Return the post feed for this Profile."""

        profilesFollowing = self.get_following()

        followingPosts = Post.objects.filter(profile__in=profilesFollowing).order_by(
            "-timestamp"
        )

        return followingPosts


class Post(models.Model):
    """Encapsulate the data of a Post by a user (Profile)"""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"profile: {self.profile}, timestamp: {self.timestamp}, caption: {self.caption}"

    def get_all_photos(self):
        """Return a QuerySet of Photos for a given Post."""

        photos = Photo.objects.filter(post=self)
        return photos

    def get_absolute_url(self):
        """Return a URL to display the updated Post."""
        return reverse("show_post", kwargs={"pk": self.pk})

    def get_all_comments(self):
        """Return a QuerySet of Comments for this Post."""

        comments = Comment.objects.filter(post=self)
        return comments

    def get_likes(self):
        """Return a QuerySet of Likes for this Post."""

        likes = Like.objects.filter(post=self)

        likeProfiles = []
        count = 0
        for like in likes:
            likeProfiles.append(like.profile)
            count += 1

        return count


class Photo(models.Model):
    """Encapsulate the data of a Photo for a Post"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(blank=True)  # an actual image

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"post: {self.post}, image_url: {self.get_image_url()}, timestamp: {self.timestamp}"

    def get_image_url(self):
        """Returns the corresponding url for the image url/file."""
        if self.image_url:
            print(self.image_url)
            return self.image_url
        else:
            print(self.image_file)
            return self.image_file.url


class Follow(models.Model):
    """Encapsulate the data of a Follower for a Profile"""

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile"
    )
    follower_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="follower_profile"
    )
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"profile: {self.profile}, profile username: {self.profile.username}, follower_profile: {self.follower_profile}, follower username: {self.follower_profile.username}, timestamp: {self.timestamp}"


class Comment(models.Model):
    """Encapsulate the data of a Comment for a Post."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=False)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"post: {self.post}, profile: {self.profile}, timestamp: {self.timestamp}, text: {self.text}"


class Like(models.Model):
    """Encapsulate the data of a Like by a Profile for a Post."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of this model instance."""
        return (
            f"post: {self.post}, profile: {self.profile}, timestamp: {self.timestamp}"
        )
