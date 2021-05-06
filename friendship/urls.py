# Copyright (c) Revolution Systems, LLC and individual contributors.
# All rights reserved.
 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
 
#     1. Redistributions of source code must retain the above copyright notice, 
#        this list of conditions and the following disclaimer.
    
#     2. Redistributions in binary form must reproduce the above copyright 
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
 
#     3. Neither the name of django-friendship nor the names of its contributors
#        may be used to endorse or promote products derived from this software
#        without specific prior written permission.
 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url
from friendship.views import (
    all_users,
    block_add,
    block_remove,
    blockers,
    blocking,
    follower_add,
    follower_remove,
    followers,
    following,
    friendship_accept,
    friendship_add_friend,
    friendship_cancel,
    friendship_reject,
    friendship_request_list,
    friendship_request_list_rejected,
    friendship_requests_detail,
    view_friends,
)

urlpatterns = [
    url(regex=r"^users/$", view=all_users, name="friendship_view_users"),
    url(
        regex=r"^friends/(?P<username>[\w-]+)/$",
        view=view_friends,
        name="friendship_view_friends",
    ),
    url(
        regex=r"^friend/add/(?P<to_username>[\w-]+)/$",
        view=friendship_add_friend,
        name="friendship_add_friend",
    ),
    url(
        regex=r"^friend/accept/(?P<friendship_request_id>\d+)/$",
        view=friendship_accept,
        name="friendship_accept",
    ),
    url(
        regex=r"^friend/reject/(?P<friendship_request_id>\d+)/$",
        view=friendship_reject,
        name="friendship_reject",
    ),
    url(
        regex=r"^friend/cancel/(?P<friendship_request_id>\d+)/$",
        view=friendship_cancel,
        name="friendship_cancel",
    ),
    url(
        regex=r"^friend/requests/$",
        view=friendship_request_list,
        name="friendship_request_list",
    ),
    url(
        regex=r"^friend/requests/rejected/$",
        view=friendship_request_list_rejected,
        name="friendship_requests_rejected",
    ),
    url(
        regex=r"^friend/request/(?P<friendship_request_id>\d+)/$",
        view=friendship_requests_detail,
        name="friendship_requests_detail",
    ),
    url(
        regex=r"^followers/(?P<username>[\w-]+)/$",
        view=followers,
        name="friendship_followers",
    ),
    url(
        regex=r"^following/(?P<username>[\w-]+)/$",
        view=following,
        name="friendship_following",
    ),
    url(
        regex=r"^follower/add/(?P<followee_username>[\w-]+)/$",
        view=follower_add,
        name="follower_add",
    ),
    url(
        regex=r"^follower/remove/(?P<followee_username>[\w-]+)/$",
        view=follower_remove,
        name="follower_remove",
    ),
    url(
        regex=r"^blockers/(?P<username>[\w-]+)/$",
        view=blockers,
        name="friendship_blockers",
    ),
    url(
        regex=r"^blocking/(?P<username>[\w-]+)/$",
        view=blocking,
        name="friendship_blocking",
    ),
    url(
        regex=r"^block/add/(?P<blocked_username>[\w-]+)/$",
        view=block_add,
        name="block_add",
    ),
    url(
        regex=r"^block/remove/(?P<blocked_username>[\w-]+)/$",
        view=block_remove,
        name="block_remove",
    ),
]
