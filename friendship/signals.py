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
from django.dispatch import Signal

friendship_request_created = Signal()
friendship_request_rejected = Signal()
friendship_request_canceled = Signal()
friendship_request_viewed = Signal()
friendship_request_accepted = Signal(providing_args=["from_user", "to_user"])
friendship_removed = Signal(providing_args=["from_user", "to_user"])
follower_created = Signal(providing_args=["follower"])
follower_removed = Signal(providing_args=["follower"])
followee_created = Signal(providing_args=["followee"])
followee_removed = Signal(providing_args=["followee"])
following_created = Signal(providing_args=["following"])
following_removed = Signal(providing_args=["following"])
block_created = Signal(providing_args=["blocker"])
block_removed = Signal(providing_args=["blocker"])
