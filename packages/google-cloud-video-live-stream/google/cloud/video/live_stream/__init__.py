# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.video.live_stream import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.video.live_stream_v1.services.livestream_service.async_client import (
    LivestreamServiceAsyncClient,
)
from google.cloud.video.live_stream_v1.services.livestream_service.client import (
    LivestreamServiceClient,
)
from google.cloud.video.live_stream_v1.types.outputs import (
    AudioStream,
    ElementaryStream,
    Manifest,
    MuxStream,
    PreprocessingConfig,
    SegmentSettings,
    SpriteSheet,
    TextStream,
    VideoStream,
)
from google.cloud.video.live_stream_v1.types.resources import (
    AudioFormat,
    AudioStreamProperty,
    Channel,
    Event,
    Input,
    InputAttachment,
    InputStreamProperty,
    LogConfig,
    VideoFormat,
    VideoStreamProperty,
)
from google.cloud.video.live_stream_v1.types.service import (
    ChannelOperationResponse,
    CreateChannelRequest,
    CreateEventRequest,
    CreateInputRequest,
    DeleteChannelRequest,
    DeleteEventRequest,
    DeleteInputRequest,
    GetChannelRequest,
    GetEventRequest,
    GetInputRequest,
    ListChannelsRequest,
    ListChannelsResponse,
    ListEventsRequest,
    ListEventsResponse,
    ListInputsRequest,
    ListInputsResponse,
    OperationMetadata,
    StartChannelRequest,
    StopChannelRequest,
    UpdateChannelRequest,
    UpdateInputRequest,
)

__all__ = (
    "LivestreamServiceClient",
    "LivestreamServiceAsyncClient",
    "AudioStream",
    "ElementaryStream",
    "Manifest",
    "MuxStream",
    "PreprocessingConfig",
    "SegmentSettings",
    "SpriteSheet",
    "TextStream",
    "VideoStream",
    "AudioFormat",
    "AudioStreamProperty",
    "Channel",
    "Event",
    "Input",
    "InputAttachment",
    "InputStreamProperty",
    "LogConfig",
    "VideoFormat",
    "VideoStreamProperty",
    "ChannelOperationResponse",
    "CreateChannelRequest",
    "CreateEventRequest",
    "CreateInputRequest",
    "DeleteChannelRequest",
    "DeleteEventRequest",
    "DeleteInputRequest",
    "GetChannelRequest",
    "GetEventRequest",
    "GetInputRequest",
    "ListChannelsRequest",
    "ListChannelsResponse",
    "ListEventsRequest",
    "ListEventsResponse",
    "ListInputsRequest",
    "ListInputsResponse",
    "OperationMetadata",
    "StartChannelRequest",
    "StopChannelRequest",
    "UpdateChannelRequest",
    "UpdateInputRequest",
)
