# Copyright (C) 2011 by Mark Visser <mjmvisser@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# This code is based on the AMD Display Library 3.0 SDK

import platform
from ctypes import *

from .adl_defines import *
from .adl_structures import *

_platform = platform.system()
_release = platform.release()

if _platform == "Linux" or _platform == "Windows":
    from ctypes import CDLL, CFUNCTYPE

    if _platform == "Linux":
        from ctypes import RTLD_GLOBAL

        # pre-load libXext (required by libatiadlxx.so in 11.12)
        CDLL("libXext.so.6", mode=RTLD_GLOBAL)

        # load the ADL 3.0 dso/dll
        _libadl = CDLL("libatiadlxx.so", mode=RTLD_GLOBAL)
    
        # ADL requires we pass an allocation function and handle freeing it ourselves
        _libc = CDLL("libc.so.6")
    else:
        from ctypes.util import find_msvcrt
        try:
            # first try to load the 64-bit library
            _libadl = CDLL("atiadlxx.dll")
        except OSError:
            # fall back on the 32-bit library
            _libadl = CDLL("atiadlxy.dll")

        _libc = CDLL(find_msvcrt());
    
    
    _malloc = _libc.malloc
    _malloc.argtypes = [c_size_t]
    _malloc.restype = c_void_p
    _free = _libc.free
    _free.argtypes = [c_void_p]

    ADL_MAIN_MALLOC_CALLBACK = CFUNCTYPE(c_void_p, c_int)
    ADL_MAIN_FREE_CALLBACK = CFUNCTYPE(None, POINTER(c_void_p))
    
    @ADL_MAIN_MALLOC_CALLBACK
    def ADL_Main_Memory_Alloc(iSize):
        return _malloc(iSize)

    @ADL_MAIN_FREE_CALLBACK
    def ADL_Main_Memory_Free(lpBuffer):
        if lpBuffer[0] is not None:
            _free(lpBuffer[0])
            lpBuffer[0] = None

else:
    raise RuntimeError("Platform '%s' is not Supported." % platform.system())

ADL_Main_Control_Create = _libadl.ADL_Main_Control_Create
ADL_Main_Control_Create.restype = c_int
ADL_Main_Control_Create.argtypes = [ADL_MAIN_MALLOC_CALLBACK, c_int]

ADL_Main_Control_Refresh = _libadl.ADL_Main_Control_Refresh
ADL_Main_Control_Refresh.restype = c_int
ADL_Main_Control_Refresh.argtypes = []

ADL_Main_Control_Destroy = _libadl.ADL_Main_Control_Destroy
ADL_Main_Control_Destroy.restype = c_int
ADL_Main_Control_Destroy.argtypes = []

ADL_Graphics_Platform_Get = _libadl.ADL_Graphics_Platform_Get
ADL_Graphics_Platform_Get.restype = c_int
ADL_Graphics_Platform_Get.argtypes = [POINTER(c_int)]

ADL_Adapter_Active_Get = _libadl.ADL_Adapter_Active_Get
ADL_Adapter_Active_Get.restype = c_int
ADL_Adapter_Active_Get.argtypes = [c_int, POINTER(c_int)]

ADL_Adapter_NumberOfAdapters_Get = _libadl.ADL_Adapter_NumberOfAdapters_Get
ADL_Adapter_NumberOfAdapters_Get.restype = c_int
ADL_Adapter_NumberOfAdapters_Get.argtypes = [POINTER(c_int)]

ADL_Adapter_AdapterInfo_Get = _libadl.ADL_Adapter_AdapterInfo_Get
ADL_Adapter_AdapterInfo_Get.restype = c_int
ADL_Adapter_AdapterInfo_Get.argtypes = [LPAdapterInfo, c_int]

ADL_Adapter_ASICFamilyType_Get = _libadl.ADL_Adapter_ASICFamilyType_Get
ADL_Adapter_ASICFamilyType_Get.restype = c_int
ADL_Adapter_ASICFamilyType_Get.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

ADL_Adapter_Speed_Caps = _libadl.ADL_Adapter_Speed_Caps
ADL_Adapter_Speed_Caps.restype = c_int
ADL_Adapter_Speed_Caps.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

ADL_Adapter_Speed_Get = _libadl.ADL_Adapter_Speed_Get
ADL_Adapter_Speed_Get.restype = c_int
ADL_Adapter_Speed_Get.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

ADL_Adapter_Speed_Set = _libadl.ADL_Adapter_Speed_Set
ADL_Adapter_Speed_Set.restype = c_int
ADL_Adapter_Speed_Set.argtypes = [c_int, c_int]

ADL_Adapter_Accessibility_Get = _libadl.ADL_Adapter_Accessibility_Get
ADL_Adapter_Accessibility_Get.restype = c_int
ADL_Adapter_Accessibility_Get.argtypes = [c_int, POINTER(c_int)]

ADL_Adapter_VideoBiosInfo_Get = _libadl.ADL_Adapter_VideoBiosInfo_Get
ADL_Adapter_VideoBiosInfo_Get.restype = c_int
ADL_Adapter_VideoBiosInfo_Get.argtypes = [c_int, POINTER(ADLBiosInfo)]

ADL_Adapter_ID_Get = _libadl.ADL_Adapter_ID_Get
ADL_Adapter_ID_Get.restype = c_int
ADL_Adapter_ID_Get.argtypes = [c_int, POINTER(c_int)]

ADL_Adapter_CrossdisplayAdapterRole_Caps = _libadl.ADL_Adapter_CrossdisplayAdapterRole_Caps
ADL_Adapter_CrossdisplayAdapterRole_Caps.restype = c_int
ADL_Adapter_CrossdisplayAdapterRole_Caps.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(c_int)]

ADL_Adapter_CrossdisplayInfo_Get = _libadl.ADL_Adapter_CrossdisplayInfo_Get
ADL_Adapter_CrossdisplayInfo_Get.restype = c_int
ADL_Adapter_CrossdisplayInfo_Get.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(c_int)]

ADL_Adapter_CrossdisplayInfo_Set = _libadl.ADL_Adapter_CrossdisplayInfo_Set
ADL_Adapter_CrossdisplayInfo_Set.restype = c_int
ADL_Adapter_CrossdisplayInfo_Set.argtypes = [c_int, c_int, c_int, c_int, POINTER(c_int)]

ADL_Adapter_Crossfire_Caps = _libadl.ADL_Adapter_Crossfire_Caps
ADL_Adapter_Crossfire_Caps.restype = c_int
ADL_Adapter_Crossfire_Caps.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(POINTER(ADLCrossfireComb))]

ADL_Adapter_Crossfire_Get = _libadl.ADL_Adapter_Crossfire_Get
ADL_Adapter_Crossfire_Get.restype = c_int
ADL_Adapter_Crossfire_Get.argtypes = [c_int, POINTER(ADLCrossfireComb), POINTER(ADLCrossfireInfo)]

ADL_Adapter_Crossfire_Set = _libadl.ADL_Adapter_Crossfire_Set
ADL_Adapter_Crossfire_Set.restype = c_int
ADL_Adapter_Crossfire_Set.argtypes = [c_int, POINTER(ADLCrossfireComb)]

ADL_Display_DisplayInfo_Get = _libadl.ADL_Display_DisplayInfo_Get
ADL_Display_DisplayInfo_Get.restype = c_int
ADL_Display_DisplayInfo_Get.argtypes = [c_int, POINTER(c_int), POINTER(POINTER(ADLDisplayInfo)), c_int]

ADL_Display_NumberOfDisplays_Get = _libadl.ADL_Display_NumberOfDisplays_Get
ADL_Display_NumberOfDisplays_Get.restype = c_int
ADL_Display_NumberOfDisplays_Get.argtypes = [c_int, POINTER(c_int)]

ADL_Display_PreservedAspectRatio_Get = _libadl.ADL_Display_PreservedAspectRatio_Get
ADL_Display_PreservedAspectRatio_Get.restype = c_int
ADL_Display_PreservedAspectRatio_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_Display_PreservedAspectRatio_Set = _libadl.ADL_Display_PreservedAspectRatio_Set
ADL_Display_PreservedAspectRatio_Set.restype = c_int
ADL_Display_PreservedAspectRatio_Set.argtypes = [c_int, c_int, c_int]

ADL_Display_ImageExpansion_Get = _libadl.ADL_Display_ImageExpansion_Get
ADL_Display_ImageExpansion_Get.restype = c_int
ADL_Display_ImageExpansion_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_Display_ImageExpansion_Set = _libadl.ADL_Display_ImageExpansion_Set
ADL_Display_ImageExpansion_Set.restype = c_int
ADL_Display_ImageExpansion_Set.argtypes = [c_int, c_int, c_int]

ADL_Display_Position_Get = _libadl.ADL_Display_Position_Get
ADL_Display_Position_Get.restype = c_int
ADL_Display_Position_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_Display_Position_Set = _libadl.ADL_Display_Position_Set
ADL_Display_Position_Set.restype = c_int
ADL_Display_Position_Set.argtypes = [c_int, c_int, c_int, c_int]

ADL_Display_Size_Get = _libadl.ADL_Display_Size_Get
ADL_Display_Size_Get.restype = c_int
ADL_Display_Size_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_Display_Size_Set = _libadl.ADL_Display_Size_Set
ADL_Display_Size_Set.restype = c_int
ADL_Display_Size_Set.argtypes = [c_int, c_int, c_int, c_int]

ADL_Display_AdjustCaps_Get = _libadl.ADL_Display_AdjustCaps_Get
ADL_Display_AdjustCaps_Get.restype = c_int
ADL_Display_AdjustCaps_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_Display_Capabilities_Get = _libadl.ADL_Display_Capabilities_Get
ADL_Display_Capabilities_Get.restype = c_int
ADL_Display_Capabilities_Get.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

ADL_Display_ConnectedDisplays_Get = _libadl.ADL_Display_ConnectedDisplays_Get
ADL_Display_ConnectedDisplays_Get.restype = c_int
ADL_Display_ConnectedDisplays_Get.argtypes = [c_int, POINTER(c_int)]

ADL_Display_DeviceConfig_Get = _libadl.ADL_Display_DeviceConfig_Get
ADL_Display_DeviceConfig_Get.restype = c_int
ADL_Display_DeviceConfig_Get.argtypes = [c_int, c_int, POINTER(ADLDisplayConfig)]

ADL_Display_Property_Get = _libadl.ADL_Display_Property_Get
ADL_Display_Property_Get.restype = c_int
ADL_Display_Property_Get.argtypes = [c_int, c_int, POINTER(ADLDisplayProperty)]

ADL_Display_Property_Set = _libadl.ADL_Display_Property_Set
ADL_Display_Property_Set.restype = c_int
ADL_Display_Property_Set.argtypes = [c_int, c_int, POINTER(ADLDisplayProperty)]

ADL_Display_SwitchingCapability_Get = _libadl.ADL_Display_SwitchingCapability_Get
ADL_Display_SwitchingCapability_Get.restype = c_int
ADL_Display_SwitchingCapability_Get.argtypes = [c_int, POINTER(c_int)]

ADL_Display_DitherState_Get = _libadl.ADL_Display_DitherState_Get
ADL_Display_DitherState_Get.restype = c_int
ADL_Display_DitherState_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_Display_DitherState_Set = _libadl.ADL_Display_DitherState_Set
ADL_Display_DitherState_Set.restype = c_int
ADL_Display_DitherState_Set.argtypes = [c_int, c_int, c_int]

ADL_Display_SupportedPixelFormat_Get = _libadl.ADL_Display_SupportedPixelFormat_Get
ADL_Display_SupportedPixelFormat_Get.restype = c_int
ADL_Display_SupportedPixelFormat_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_Display_PixelFormat_Get = _libadl.ADL_Display_PixelFormat_Get
ADL_Display_PixelFormat_Get.restype = c_int
ADL_Display_PixelFormat_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_Display_PixelFormat_Set = _libadl.ADL_Display_PixelFormat_Set
ADL_Display_PixelFormat_Set.restype = c_int
ADL_Display_PixelFormat_Set.argtypes = [c_int, c_int, c_int]

ADL_Display_ODClockInfo_Get = _libadl.ADL_Display_ODClockInfo_Get
ADL_Display_ODClockInfo_Get.restype = c_int
ADL_Display_ODClockInfo_Get.argtypes = [c_int, POINTER(ADLAdapterODClockInfo)]

ADL_Display_ODClockConfig_Set = _libadl.ADL_Display_ODClockConfig_Set
ADL_Display_ODClockConfig_Set.restype = c_int
ADL_Display_ODClockConfig_Set.argtypes = [c_int, POINTER(ADLAdapterODClockConfig)]

ADL_Display_AdjustmentCoherent_Get = _libadl.ADL_Display_AdjustmentCoherent_Get
ADL_Display_AdjustmentCoherent_Get.restype = c_int
ADL_Display_AdjustmentCoherent_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int)]

ADL_Display_AdjustmentCoherent_Set = _libadl.ADL_Display_AdjustmentCoherent_Set
ADL_Display_AdjustmentCoherent_Set.restype = c_int
ADL_Display_AdjustmentCoherent_Set.argtypes = [c_int, c_int, c_int]

ADL_Display_ReducedBlanking_Get = _libadl.ADL_Display_ReducedBlanking_Get
ADL_Display_ReducedBlanking_Get.restype = c_int
ADL_Display_ReducedBlanking_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int)]

ADL_Display_ReducedBlanking_Set = _libadl.ADL_Display_ReducedBlanking_Set
ADL_Display_ReducedBlanking_Set.restype = c_int
ADL_Display_ReducedBlanking_Set.argtypes = [c_int, c_int, c_int]

ADL_Display_FormatsOverride_Get = _libadl.ADL_Display_FormatsOverride_Get
ADL_Display_FormatsOverride_Get.restype = c_int
ADL_Display_FormatsOverride_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_Display_FormatsOverride_Set = _libadl.ADL_Display_FormatsOverride_Set
ADL_Display_FormatsOverride_Set.restype = c_int
ADL_Display_FormatsOverride_Set.argtypes = [c_int, c_int, c_int]

ADL_Display_MVPUCaps_Get = _libadl.ADL_Display_MVPUCaps_Get
ADL_Display_MVPUCaps_Get.restype = c_int
ADL_Display_MVPUCaps_Get.argtypes = [c_int, POINTER(ADLMVPUCaps)]

ADL_Display_MVPUStatus_Get = _libadl.ADL_Display_MVPUStatus_Get
ADL_Display_MVPUStatus_Get.restype = c_int
ADL_Display_MVPUStatus_Get.argtypes = [c_int, POINTER(ADLMVPUStatus)]

ADL_Adapter_Active_Set = _libadl.ADL_Adapter_Active_Set
ADL_Adapter_Active_Set.restype = c_int
ADL_Adapter_Active_Set.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_Adapter_Active_SetPrefer = _libadl.ADL_Adapter_Active_SetPrefer
ADL_Adapter_Active_SetPrefer.restype = c_int
ADL_Adapter_Active_SetPrefer.argtypes = [c_int, c_int, c_int, POINTER(ADLDisplayTarget), POINTER(c_int)]

ADL_Adapter_Primary_Get = _libadl.ADL_Adapter_Primary_Get
ADL_Adapter_Primary_Get.restype = c_int
ADL_Adapter_Primary_Get.argtypes = [POINTER(c_int)]

ADL_Adapter_Primary_Set = _libadl.ADL_Adapter_Primary_Set
ADL_Adapter_Primary_Set.restype = c_int
ADL_Adapter_Primary_Set.argtypes = [c_int]

ADL_Adapter_ModeSwitch = _libadl.ADL_Adapter_ModeSwitch
ADL_Adapter_ModeSwitch.restype = c_int
ADL_Adapter_ModeSwitch.argtypes = [c_int]

ADL_Display_Modes_Get = _libadl.ADL_Display_Modes_Get
ADL_Display_Modes_Get.restype = c_int
ADL_Display_Modes_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(POINTER(ADLMode))]

ADL_Display_Modes_Set = _libadl.ADL_Display_Modes_Set
ADL_Display_Modes_Set.restype = c_int
ADL_Display_Modes_Set.argtypes = [c_int, c_int, c_int, POINTER(ADLMode)]

ADL_Display_PossibleMode_Get = _libadl.ADL_Display_PossibleMode_Get
ADL_Display_PossibleMode_Get.restype = c_int
ADL_Display_PossibleMode_Get.argtypes = [c_int, POINTER(c_int), POINTER(POINTER(ADLMode))]

ADL_Display_ForcibleDisplay_Get = _libadl.ADL_Display_ForcibleDisplay_Get
ADL_Display_ForcibleDisplay_Get.restype = c_int
ADL_Display_ForcibleDisplay_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_Display_ForcibleDisplay_Set = _libadl.ADL_Display_ForcibleDisplay_Set
ADL_Display_ForcibleDisplay_Set.restype = c_int
ADL_Display_ForcibleDisplay_Set.argtypes = [c_int, c_int, c_int]

ADL_Adapter_NumberOfActivatableSources_Get = _libadl.ADL_Adapter_NumberOfActivatableSources_Get
ADL_Adapter_NumberOfActivatableSources_Get.restype = c_int
ADL_Adapter_NumberOfActivatableSources_Get.argtypes = [c_int, POINTER(c_int), POINTER(POINTER(ADLActivatableSource))]

ADL_Adapter_Display_Caps = _libadl.ADL_Adapter_Display_Caps
ADL_Adapter_Display_Caps.restype = c_int
ADL_Adapter_Display_Caps.argtypes = [c_int, POINTER(c_int), POINTER(POINTER(ADLAdapterDisplayCap))]

ADL_Display_DisplayMapConfig_Get = _libadl.ADL_Display_DisplayMapConfig_Get
ADL_Display_DisplayMapConfig_Get.restype = c_int
ADL_Display_DisplayMapConfig_Get.argtypes = [c_int, POINTER(c_int), POINTER(POINTER(ADLDisplayMap)), POINTER(c_int), POINTER(POINTER(ADLDisplayTarget)), c_int]

ADL_Display_DisplayMapConfig_Set = _libadl.ADL_Display_DisplayMapConfig_Set
ADL_Display_DisplayMapConfig_Set.restype = c_int
ADL_Display_DisplayMapConfig_Set.argtypes = [c_int, c_int, POINTER(ADLDisplayMap), c_int, POINTER(ADLDisplayTarget)]

ADL_Display_PossibleMapping_Get = _libadl.ADL_Display_PossibleMapping_Get
ADL_Display_PossibleMapping_Get.restype = c_int
ADL_Display_PossibleMapping_Get.argtypes = [c_int, c_int, POINTER(ADLPossibleMapping), c_int, POINTER(c_int), POINTER(POINTER(ADLPossibleMapping))]

ADL_Display_DisplayMapConfig_Validate = _libadl.ADL_Display_DisplayMapConfig_Validate
ADL_Display_DisplayMapConfig_Validate.restype = c_int
ADL_Display_DisplayMapConfig_Validate.argtypes = [c_int, c_int, POINTER(ADLPossibleMap), POINTER(c_int), POINTER(POINTER(ADLPossibleMapResult))]

ADL_Display_DisplayMapConfig_PossibleAddAndRemove = _libadl.ADL_Display_DisplayMapConfig_PossibleAddAndRemove
ADL_Display_DisplayMapConfig_PossibleAddAndRemove.restype = c_int
ADL_Display_DisplayMapConfig_PossibleAddAndRemove.argtypes = [c_int, c_int, POINTER(ADLDisplayMap), c_int, POINTER(ADLDisplayTarget), POINTER(c_int), POINTER(POINTER(ADLDisplayTarget)), POINTER(c_int), POINTER(POINTER(ADLDisplayTarget))]

ADL_Display_SLSGrid_Caps = _libadl.ADL_Display_SLSGrid_Caps
ADL_Display_SLSGrid_Caps.restype = c_int
ADL_Display_SLSGrid_Caps.argtypes = [c_int, POINTER(c_int), POINTER(POINTER(ADLSLSGrid)), c_int]

ADL_Display_SLSMapIndexList_Get = _libadl.ADL_Display_SLSMapIndexList_Get
ADL_Display_SLSMapIndexList_Get.restype = c_int
ADL_Display_SLSMapIndexList_Get.argtypes = [c_int, POINTER(c_int), POINTER(POINTER(c_int)), c_int]

ADL_Display_SLSMapIndex_Get = _libadl.ADL_Display_SLSMapIndex_Get
ADL_Display_SLSMapIndex_Get.restype = c_int
ADL_Display_SLSMapIndex_Get.argtypes = [c_int, c_int, POINTER(ADLDisplayTarget), POINTER(c_int)]

ADL_Display_SLSMapConfig_Get = _libadl.ADL_Display_SLSMapConfig_Get
ADL_Display_SLSMapConfig_Get.restype = c_int
ADL_Display_SLSMapConfig_Get.argtypes = [c_int, c_int, POINTER(ADLSLSMap), POINTER(c_int), POINTER(POINTER(ADLSLSTarget)), POINTER(c_int), POINTER(POINTER(ADLSLSMode)), POINTER(c_int), POINTER(POINTER(ADLBezelTransientMode)), POINTER(c_int), POINTER(POINTER(ADLBezelTransientMode)), POINTER(c_int), POINTER(POINTER(ADLSLSOffset)), c_int]

ADL_Display_SLSMapConfig_Create = _libadl.ADL_Display_SLSMapConfig_Create
ADL_Display_SLSMapConfig_Create.restype = c_int
ADL_Display_SLSMapConfig_Create.argtypes = [c_int, ADLSLSMap, c_int, POINTER(ADLSLSTarget), c_int, POINTER(c_int), c_int]

ADL_Display_SLSMapConfig_Delete = _libadl.ADL_Display_SLSMapConfig_Delete
ADL_Display_SLSMapConfig_Delete.restype = c_int
ADL_Display_SLSMapConfig_Delete.argtypes = [c_int, c_int]

ADL_Display_SLSMapConfig_SetState = _libadl.ADL_Display_SLSMapConfig_SetState
ADL_Display_SLSMapConfig_SetState.restype = c_int
ADL_Display_SLSMapConfig_SetState.argtypes = [c_int, c_int, c_int]

ADL_Display_SLSMapConfig_Rearrange = _libadl.ADL_Display_SLSMapConfig_Rearrange
ADL_Display_SLSMapConfig_Rearrange.restype = c_int
ADL_Display_SLSMapConfig_Rearrange.argtypes = [c_int, c_int, c_int, POINTER(ADLSLSTarget), ADLSLSMap, c_int]

if _platform == "Windows" and _release == "XP":
    ADL_Display_PossibleMode_WinXP_Get = _libadl.ADL_Display_PossibleMode_WinXP_Get
    ADL_Display_PossibleMode_WinXP_Get.restype = c_int
    ADL_Display_PossibleMode_WinXP_Get.argtypes = [c_int, c_int, POINTER(ADLDisplayTarget), c_int, c_int, POINTER(c_int), POINTER(POINTER(ADLMode))]

ADL_Display_BezelOffsetSteppingSize_Get = _libadl.ADL_Display_BezelOffsetSteppingSize_Get
ADL_Display_BezelOffsetSteppingSize_Get.restype = c_int
ADL_Display_BezelOffsetSteppingSize_Get.argtypes = [c_int, POINTER(c_int), POINTER(POINTER(ADLBezelOffsetSteppingSize))]

ADL_Display_BezelOffset_Set = _libadl.ADL_Display_BezelOffset_Set
ADL_Display_BezelOffset_Set.restype = c_int
ADL_Display_BezelOffset_Set.argtypes = [c_int, c_int, c_int, LPADLSLSOffset, ADLSLSMap, c_int]

ADL_Display_BezelSupported_Validate = _libadl.ADL_Display_BezelSupported_Validate
ADL_Display_BezelSupported_Validate.restype = c_int
ADL_Display_BezelSupported_Validate.argtypes = [c_int, c_int, LPADLPossibleSLSMap, POINTER(c_int), POINTER(LPADLPossibleMapResult)]

ADL_Display_ColorCaps_Get = _libadl.ADL_Display_ColorCaps_Get
ADL_Display_ColorCaps_Get.restype = c_int
ADL_Display_ColorCaps_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int)]

ADL_Display_Color_Set = _libadl.ADL_Display_Color_Set
ADL_Display_Color_Set.restype = c_int
ADL_Display_Color_Set.argtypes = [c_int, c_int, c_int, c_int]

ADL_Display_Color_Get = _libadl.ADL_Display_Color_Get
ADL_Display_Color_Get.restype = c_int
ADL_Display_Color_Get.argtypes = [c_int, c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_Display_ColorTemperatureSource_Get = _libadl.ADL_Display_ColorTemperatureSource_Get
ADL_Display_ColorTemperatureSource_Get.restype = c_int
ADL_Display_ColorTemperatureSource_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_Display_ColorTemperatureSource_Set = _libadl.ADL_Display_ColorTemperatureSource_Set
ADL_Display_ColorTemperatureSource_Set.restype = c_int
ADL_Display_ColorTemperatureSource_Set.argtypes = [c_int, c_int, c_int]

ADL_Display_ModeTimingOverride_Get = _libadl.ADL_Display_ModeTimingOverride_Get
ADL_Display_ModeTimingOverride_Get.restype = c_int
ADL_Display_ModeTimingOverride_Get.argtypes = [c_int, c_int, POINTER(ADLDisplayMode), POINTER(ADLDisplayModeInfo)]

ADL_Display_ModeTimingOverride_Set = _libadl.ADL_Display_ModeTimingOverride_Set
ADL_Display_ModeTimingOverride_Set.restype = c_int
ADL_Display_ModeTimingOverride_Set.argtypes = [c_int, c_int, POINTER(ADLDisplayModeInfo), c_int]

ADL_Display_ModeTimingOverrideList_Get = _libadl.ADL_Display_ModeTimingOverrideList_Get
ADL_Display_ModeTimingOverrideList_Get.restype = c_int
ADL_Display_ModeTimingOverrideList_Get.argtypes = [c_int, c_int, c_int, POINTER(ADLDisplayModeInfo), POINTER(c_int)]

ADL_Display_CustomizedModeListNum_Get = _libadl.ADL_Display_CustomizedModeListNum_Get
ADL_Display_CustomizedModeListNum_Get.restype = c_int
ADL_Display_CustomizedModeListNum_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_Display_CustomizedModeList_Get = _libadl.ADL_Display_CustomizedModeList_Get
ADL_Display_CustomizedModeList_Get.restype = c_int
ADL_Display_CustomizedModeList_Get.argtypes = [c_int, c_int, POINTER(ADLCustomMode), c_int]

ADL_Display_CustomizedMode_Add = _libadl.ADL_Display_CustomizedMode_Add
ADL_Display_CustomizedMode_Add.restype = c_int
ADL_Display_CustomizedMode_Add.argtypes = [c_int, c_int, ADLCustomMode]

ADL_Display_CustomizedMode_Delete = _libadl.ADL_Display_CustomizedMode_Delete
ADL_Display_CustomizedMode_Delete.restype = c_int
ADL_Display_CustomizedMode_Delete.argtypes = [c_int, c_int, c_int]

ADL_Display_CustomizedMode_Validate = _libadl.ADL_Display_CustomizedMode_Validate
ADL_Display_CustomizedMode_Validate.restype = c_int
ADL_Display_CustomizedMode_Validate.argtypes = [c_int, c_int, ADLCustomMode, POINTER(c_int)]

ADL_Display_Underscan_Set = _libadl.ADL_Display_Underscan_Set
ADL_Display_Underscan_Set.restype = c_int
ADL_Display_Underscan_Set.argtypes = [c_int, c_int, c_int]

ADL_Display_Underscan_Get = _libadl.ADL_Display_Underscan_Get
ADL_Display_Underscan_Get.restype = c_int
ADL_Display_Underscan_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_Display_Overscan_Set = _libadl.ADL_Display_Overscan_Set
ADL_Display_Overscan_Set.restype = c_int
ADL_Display_Overscan_Set.argtypes = [c_int, c_int, c_int]

ADL_Display_Overscan_Get = _libadl.ADL_Display_Overscan_Get
ADL_Display_Overscan_Get.restype = c_int
ADL_Display_Overscan_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_Display_ControllerOverlayAdjustmentCaps_Get = _libadl.ADL_Display_ControllerOverlayAdjustmentCaps_Get
ADL_Display_ControllerOverlayAdjustmentCaps_Get.restype = c_int
ADL_Display_ControllerOverlayAdjustmentCaps_Get.argtypes = [c_int, POINTER(ADLControllerOverlayInput), POINTER(ADLControllerOverlayInfo)]

ADL_Display_ControllerOverlayAdjustmentData_Get = _libadl.ADL_Display_ControllerOverlayAdjustmentData_Get
ADL_Display_ControllerOverlayAdjustmentData_Get.restype = c_int
ADL_Display_ControllerOverlayAdjustmentData_Get.argtypes = [c_int, POINTER(ADLControllerOverlayInput)]

ADL_Display_ControllerOverlayAdjustmentData_Set = _libadl.ADL_Display_ControllerOverlayAdjustmentData_Set
ADL_Display_ControllerOverlayAdjustmentData_Set.restype = c_int
ADL_Display_ControllerOverlayAdjustmentData_Set.argtypes = [c_int, POINTER(ADLControllerOverlayInput)]

ADL_Display_PowerXpressVersion_Get = _libadl.ADL_Display_PowerXpressVersion_Get
ADL_Display_PowerXpressVersion_Get.restype = c_int
ADL_Display_PowerXpressVersion_Get.argtypes = [c_int, POINTER(c_int)]

ADL_Display_PowerXpressActiveGPU_Get = _libadl.ADL_Display_PowerXpressActiveGPU_Get
ADL_Display_PowerXpressActiveGPU_Get.restype = c_int
ADL_Display_PowerXpressActiveGPU_Get.argtypes = [c_int, POINTER(c_int)]

ADL_Display_PowerXpressActiveGPU_Set = _libadl.ADL_Display_PowerXpressActiveGPU_Set
ADL_Display_PowerXpressActiveGPU_Set.restype = c_int
ADL_Display_PowerXpressActiveGPU_Set.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_Display_PowerXpress_AutoSwitchConfig_Get = _libadl.ADL_Display_PowerXpress_AutoSwitchConfig_Get
ADL_Display_PowerXpress_AutoSwitchConfig_Get.restype = c_int
ADL_Display_PowerXpress_AutoSwitchConfig_Get.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

ADL_Display_PowerXpress_AutoSwitchConfig_Set = _libadl.ADL_Display_PowerXpress_AutoSwitchConfig_Set
ADL_Display_PowerXpress_AutoSwitchConfig_Set.restype = c_int
ADL_Display_PowerXpress_AutoSwitchConfig_Set.argtypes = [c_int, c_int, c_int]

ADL_DFP_BaseAudioSupport_Get = _libadl.ADL_DFP_BaseAudioSupport_Get
ADL_DFP_BaseAudioSupport_Get.restype = c_int
ADL_DFP_BaseAudioSupport_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_DFP_HDMISupport_Get = _libadl.ADL_DFP_HDMISupport_Get
ADL_DFP_HDMISupport_Get.restype = c_int
ADL_DFP_HDMISupport_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_DFP_MVPUAnalogSupport_Get = _libadl.ADL_DFP_MVPUAnalogSupport_Get
ADL_DFP_MVPUAnalogSupport_Get.restype = c_int
ADL_DFP_MVPUAnalogSupport_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_DFP_PixelFormat_Caps = _libadl.ADL_DFP_PixelFormat_Caps
ADL_DFP_PixelFormat_Caps.restype = c_int
ADL_DFP_PixelFormat_Caps.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int)]

ADL_DFP_PixelFormat_Get = _libadl.ADL_DFP_PixelFormat_Get
ADL_DFP_PixelFormat_Get.restype = c_int
ADL_DFP_PixelFormat_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int)]

ADL_DFP_PixelFormat_Set = _libadl.ADL_DFP_PixelFormat_Set
ADL_DFP_PixelFormat_Set.restype = c_int
ADL_DFP_PixelFormat_Set.argtypes = [c_int, c_int, c_int]

ADL_DFP_GPUScalingEnable_Get = _libadl.ADL_DFP_GPUScalingEnable_Get
ADL_DFP_GPUScalingEnable_Get.restype = c_int
ADL_DFP_GPUScalingEnable_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_DFP_GPUScalingEnable_Set = _libadl.ADL_DFP_GPUScalingEnable_Set
ADL_DFP_GPUScalingEnable_Set.restype = c_int
ADL_DFP_GPUScalingEnable_Set.argtypes = [c_int, c_int, c_int]

ADL_DFP_AllowOnlyCETimings_Get = _libadl.ADL_DFP_AllowOnlyCETimings_Get
ADL_DFP_AllowOnlyCETimings_Get.restype = c_int
ADL_DFP_AllowOnlyCETimings_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_DFP_AllowOnlyCETimings_Set = _libadl.ADL_DFP_AllowOnlyCETimings_Set
ADL_DFP_AllowOnlyCETimings_Set.restype = c_int
ADL_DFP_AllowOnlyCETimings_Set.argtypes = [c_int, c_int, c_int]

ADL_Display_TVCaps_Get = _libadl.ADL_Display_TVCaps_Get
ADL_Display_TVCaps_Get.restype = c_int
ADL_Display_TVCaps_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_TV_Standard_Set = _libadl.ADL_TV_Standard_Set
ADL_TV_Standard_Set.restype = c_int
ADL_TV_Standard_Set.argtypes = [c_int, c_int, c_int]

ADL_TV_Standard_Get = _libadl.ADL_TV_Standard_Get
ADL_TV_Standard_Get.restype = c_int
ADL_TV_Standard_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_CV_DongleSettings_Get = _libadl.ADL_CV_DongleSettings_Get
ADL_CV_DongleSettings_Get.restype = c_int
ADL_CV_DongleSettings_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_CV_DongleSettings_Set = _libadl.ADL_CV_DongleSettings_Set
ADL_CV_DongleSettings_Set.restype = c_int
ADL_CV_DongleSettings_Set.argtypes = [c_int, c_int, c_int]

ADL_CV_DongleSettings_Reset = _libadl.ADL_CV_DongleSettings_Reset
ADL_CV_DongleSettings_Reset.restype = c_int
ADL_CV_DongleSettings_Reset.argtypes = [c_int, c_int]

ADL_Overdrive5_CurrentActivity_Get = _libadl.ADL_Overdrive5_CurrentActivity_Get
ADL_Overdrive5_CurrentActivity_Get.restype = c_int
ADL_Overdrive5_CurrentActivity_Get.argtypes = [c_int, POINTER(ADLPMActivity)]

ADL_Overdrive5_ThermalDevices_Enum = _libadl.ADL_Overdrive5_ThermalDevices_Enum
ADL_Overdrive5_ThermalDevices_Enum.restype = c_int
ADL_Overdrive5_ThermalDevices_Enum.argtypes = [c_int, c_int, POINTER(ADLThermalControllerInfo)]

ADL_Overdrive5_Temperature_Get = _libadl.ADL_Overdrive5_Temperature_Get
ADL_Overdrive5_Temperature_Get.restype = c_int
ADL_Overdrive5_Temperature_Get.argtypes = [c_int, c_int, POINTER(ADLTemperature)]

ADL_Overdrive5_FanSpeedInfo_Get = _libadl.ADL_Overdrive5_FanSpeedInfo_Get
ADL_Overdrive5_FanSpeedInfo_Get.restype = c_int
ADL_Overdrive5_FanSpeedInfo_Get.argtypes = [c_int, c_int, POINTER(ADLFanSpeedInfo)]

ADL_Overdrive5_FanSpeed_Get = _libadl.ADL_Overdrive5_FanSpeed_Get
ADL_Overdrive5_FanSpeed_Get.restype = c_int
ADL_Overdrive5_FanSpeed_Get.argtypes = [c_int, c_int, POINTER(ADLFanSpeedValue)]

ADL_Overdrive5_FanSpeed_Set = _libadl.ADL_Overdrive5_FanSpeed_Set
ADL_Overdrive5_FanSpeed_Set.restype = c_int
ADL_Overdrive5_FanSpeed_Set.argtypes = [c_int, c_int, POINTER(ADLFanSpeedValue)]

ADL_Overdrive5_FanSpeedToDefault_Set = _libadl.ADL_Overdrive5_FanSpeedToDefault_Set
ADL_Overdrive5_FanSpeedToDefault_Set.restype = c_int
ADL_Overdrive5_FanSpeedToDefault_Set.argtypes = [c_int, c_int]

ADL_Overdrive5_ODParameters_Get = _libadl.ADL_Overdrive5_ODParameters_Get
ADL_Overdrive5_ODParameters_Get.restype = c_int
ADL_Overdrive5_ODParameters_Get.argtypes = [c_int, POINTER(ADLODParameters)]

ADL_Overdrive5_ODPerformanceLevels_Get = _libadl.ADL_Overdrive5_ODPerformanceLevels_Get
ADL_Overdrive5_ODPerformanceLevels_Get.restype = c_int
ADL_Overdrive5_ODPerformanceLevels_Get.argtypes = [c_int, c_int, POINTER(ADLODPerformanceLevels)]

ADL_Overdrive5_ODPerformanceLevels_Set = _libadl.ADL_Overdrive5_ODPerformanceLevels_Set
ADL_Overdrive5_ODPerformanceLevels_Set.restype = c_int
ADL_Overdrive5_ODPerformanceLevels_Set.argtypes = [c_int, POINTER(ADLODPerformanceLevels)]

# PowerControl APIs are undocumented, discovered via the AMDOverdriveCtrl project
# http://phoronix.com/forums/showthread.php?55589-undocumented-feature-powertune
ADL_Overdrive5_PowerControl_Get = _libadl.ADL_Overdrive5_PowerControl_Get
ADL_Overdrive5_PowerControl_Get.restype = c_int
ADL_Overdrive5_PowerControl_Get.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

ADL_Overdrive5_PowerControl_Set = _libadl.ADL_Overdrive5_PowerControl_Set
ADL_Overdrive5_PowerControl_Set.restype = c_int
ADL_Overdrive5_PowerControl_Set.argtypes = [c_int, c_int]

ADL_Overdrive5_PowerControl_Caps = _libadl.ADL_Overdrive5_PowerControl_Caps
ADL_Overdrive5_PowerControl_Caps.restype = c_int
ADL_Overdrive5_PowerControl_Caps.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

ADL_Overdrive5_PowerControlInfo_Get = _libadl.ADL_Overdrive5_PowerControlInfo_Get
ADL_Overdrive5_PowerControlInfo_Get.restype = c_int
ADL_Overdrive5_PowerControlInfo_Get.argtypes = [c_int]

ADL_Display_WriteAndReadI2CRev_Get = _libadl.ADL_Display_WriteAndReadI2CRev_Get
ADL_Display_WriteAndReadI2CRev_Get.restype = c_int
ADL_Display_WriteAndReadI2CRev_Get.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

ADL_Display_WriteAndReadI2C = _libadl.ADL_Display_WriteAndReadI2C
ADL_Display_WriteAndReadI2C.restype = c_int
ADL_Display_WriteAndReadI2C.argtypes = [c_int, POINTER(ADLI2C)]

ADL_Display_DDCBlockAccess_Get = _libadl.ADL_Display_DDCBlockAccess_Get
ADL_Display_DDCBlockAccess_Get.restype = c_int
ADL_Display_DDCBlockAccess_Get.argtypes = [c_int, c_int, c_int, c_int, c_int, c_char_p, POINTER(c_int), c_char_p]

ADL_Display_DDCInfo_Get = _libadl.ADL_Display_DDCInfo_Get
ADL_Display_DDCInfo_Get.restype = c_int
ADL_Display_DDCInfo_Get.argtypes = [c_int, c_int, POINTER(ADLDDCInfo)]

ADL_Display_EdidData_Get = _libadl.ADL_Display_EdidData_Get
ADL_Display_EdidData_Get.restype = c_int
ADL_Display_EdidData_Get.argtypes = [c_int, c_int, POINTER(ADLDisplayEDIDData)]

ADL_Workstation_Caps = _libadl.ADL_Workstation_Caps
ADL_Workstation_Caps.restype = c_int
ADL_Workstation_Caps.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

ADL_Workstation_Stereo_Get = _libadl.ADL_Workstation_Stereo_Get
ADL_Workstation_Stereo_Get.restype = c_int
ADL_Workstation_Stereo_Get.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

ADL_Workstation_Stereo_Set = _libadl.ADL_Workstation_Stereo_Set
ADL_Workstation_Stereo_Set.restype = c_int
ADL_Workstation_Stereo_Set.argtypes = [c_int, c_int]

ADL_Workstation_AdapterNumOfGLSyncConnectors_Get = _libadl.ADL_Workstation_AdapterNumOfGLSyncConnectors_Get
ADL_Workstation_AdapterNumOfGLSyncConnectors_Get.restype = c_int
ADL_Workstation_AdapterNumOfGLSyncConnectors_Get.argtypes = [c_int, POINTER(c_int)]

ADL_Workstation_DisplayGenlockCapable_Get = _libadl.ADL_Workstation_DisplayGenlockCapable_Get
ADL_Workstation_DisplayGenlockCapable_Get.restype = c_int
ADL_Workstation_DisplayGenlockCapable_Get.argtypes = [c_int, c_int, POINTER(c_int)]

ADL_Workstation_GLSyncModuleDetect_Get = _libadl.ADL_Workstation_GLSyncModuleDetect_Get
ADL_Workstation_GLSyncModuleDetect_Get.restype = c_int
ADL_Workstation_GLSyncModuleDetect_Get.argtypes = [c_int, c_int, POINTER(ADLGLSyncModuleID)]

ADL_Workstation_GLSyncModuleInfo_Get = _libadl.ADL_Workstation_GLSyncModuleInfo_Get
ADL_Workstation_GLSyncModuleInfo_Get.restype = c_int
ADL_Workstation_GLSyncModuleInfo_Get.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(POINTER(ADLGLSyncPortCaps))]

ADL_Workstation_GLSyncGenlockConfiguration_Get = _libadl.ADL_Workstation_GLSyncGenlockConfiguration_Get
ADL_Workstation_GLSyncGenlockConfiguration_Get.restype = c_int
ADL_Workstation_GLSyncGenlockConfiguration_Get.argtypes = [c_int, c_int, c_int, POINTER(ADLGLSyncGenlockConfig)]

ADL_Workstation_GLSyncGenlockConfiguration_Set = _libadl.ADL_Workstation_GLSyncGenlockConfiguration_Set
ADL_Workstation_GLSyncGenlockConfiguration_Set.restype = c_int
ADL_Workstation_GLSyncGenlockConfiguration_Set.argtypes = [c_int, c_int, ADLGLSyncGenlockConfig]

ADL_Workstation_GLSyncPortState_Get = _libadl.ADL_Workstation_GLSyncPortState_Get
ADL_Workstation_GLSyncPortState_Get.restype = c_int
ADL_Workstation_GLSyncPortState_Get.argtypes = [c_int, c_int, c_int, c_int, POINTER(ADLGlSyncPortInfo), POINTER(POINTER(c_int))]

ADL_Workstation_GLSyncPortState_Set = _libadl.ADL_Workstation_GLSyncPortState_Set
ADL_Workstation_GLSyncPortState_Set.restype = c_int
ADL_Workstation_GLSyncPortState_Set.argtypes = [c_int, c_int, ADLGlSyncPortControl]

ADL_Workstation_DisplayGLSyncMode_Get = _libadl.ADL_Workstation_DisplayGLSyncMode_Get
ADL_Workstation_DisplayGLSyncMode_Get.restype = c_int
ADL_Workstation_DisplayGLSyncMode_Get.argtypes = [c_int, c_int, POINTER(ADLGlSyncMode)]

ADL_Workstation_DisplayGLSyncMode_Set = _libadl.ADL_Workstation_DisplayGLSyncMode_Set
ADL_Workstation_DisplayGLSyncMode_Set.restype = c_int
ADL_Workstation_DisplayGLSyncMode_Set.argtypes = [c_int, c_int, ADLGlSyncMode]

ADL_Workstation_GLSyncSupportedTopology_Get = _libadl.ADL_Workstation_GLSyncSupportedTopology_Get
ADL_Workstation_GLSyncSupportedTopology_Get.restype = c_int
ADL_Workstation_GLSyncSupportedTopology_Get.argtypes = [c_int, c_int, POINTER(ADLGlSyncMode2), POINTER(c_int), POINTER(POINTER(ADLGlSyncMode2))]

ADL_Workstation_LoadBalancing_Get = _libadl.ADL_Workstation_LoadBalancing_Get
ADL_Workstation_LoadBalancing_Get.restype = c_int
ADL_Workstation_LoadBalancing_Get.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]

ADL_Workstation_LoadBalancing_Set = _libadl.ADL_Workstation_LoadBalancing_Set
ADL_Workstation_LoadBalancing_Set.restype = c_int
ADL_Workstation_LoadBalancing_Set.argtypes = [c_int]

ADL_Workstation_LoadBalancing_Caps = _libadl.ADL_Workstation_LoadBalancing_Caps
ADL_Workstation_LoadBalancing_Caps.restype = c_int
ADL_Workstation_LoadBalancing_Caps.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

if _platform == "Linux":
    ADL_Adapter_MemoryInfo_Get = _libadl.ADL_Adapter_MemoryInfo_Get
    ADL_Adapter_MemoryInfo_Get.restype = c_int
    ADL_Adapter_MemoryInfo_Get.argtypes = [c_int, POINTER(ADLMemoryInfo)]
    
    # missing in linux dso, but listed in the API docs
    #ADL_Controller_Color_Set = _libadl.ADL_Controller_Color_Set
    #ADL_Controller_Color_Set.restype = c_int
    #ADL_Controller_Color_Set.argtypes = [c_int, c_int, ADLGamma]
    
    #ADL_Controller_Color_Get = _libadl.ADL_Controller_Color_Get
    #ADL_Controller_Color_Get.restype = c_int
    #ADL_Controller_Color_Get.argtypes = [c_int, c_int, POINTER(ADLGamma), POINTER(ADLGamma), POINTER(ADLGamma), POINTER(ADLGamma)]
    
    ADL_DesktopConfig_Get = _libadl.ADL_DesktopConfig_Get
    ADL_DesktopConfig_Get.restype = c_int
    ADL_DesktopConfig_Get.argtypes = [c_int, POINTER(c_int)]
    
    ADL_DesktopConfig_Set = _libadl.ADL_DesktopConfig_Set
    ADL_DesktopConfig_Set.restype = c_int
    ADL_DesktopConfig_Set.argtypes = [c_int, c_int]
    
    ADL_NumberOfDisplayEnable_Get = _libadl.ADL_NumberOfDisplayEnable_Get
    ADL_NumberOfDisplayEnable_Get.restype = c_int
    ADL_NumberOfDisplayEnable_Get.argtypes = [c_int, POINTER(c_int)]
    
    ADL_DisplayEnable_Set = _libadl.ADL_DisplayEnable_Set
    ADL_DisplayEnable_Set.restype = c_int
    ADL_DisplayEnable_Set.argtypes = [c_int, POINTER(c_int), c_int, c_int]
    
    ADL_Display_IdentifyDisplay = _libadl.ADL_Display_IdentifyDisplay
    ADL_Display_IdentifyDisplay.restype = c_int
    ADL_Display_IdentifyDisplay.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int]
    
    ADL_Display_LUTColor_Set = _libadl.ADL_Display_LUTColor_Set
    ADL_Display_LUTColor_Set.restype = c_int
    ADL_Display_LUTColor_Set.argtypes = [c_int, c_int, ADLGamma]
    
    ADL_Display_LUTColor_Get = _libadl.ADL_Display_LUTColor_Get
    ADL_Display_LUTColor_Get.restype = c_int
    ADL_Display_LUTColor_Get.argtypes = [c_int, c_int, POINTER(ADLGamma), POINTER(ADLGamma), POINTER(ADLGamma), POINTER(ADLGamma)]
    
    ADL_Adapter_XScreenInfo_Get = _libadl.ADL_Adapter_XScreenInfo_Get
    ADL_Adapter_XScreenInfo_Get.restype = c_int
    ADL_Adapter_XScreenInfo_Get.argtypes = [LPXScreenInfo, c_int]
    
    ADL_Display_XrandrDisplayName_Get = _libadl.ADL_Display_XrandrDisplayName_Get
    ADL_Display_XrandrDisplayName_Get.restype = c_int
    ADL_Display_XrandrDisplayName_Get.argtypes = [c_int, c_int, c_char_p, c_int]

