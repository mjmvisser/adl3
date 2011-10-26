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

from ctypes import Structure, POINTER
from ctypes import c_int, c_float, c_char, c_char_p, c_short, c_long, c_longlong
import platform

_platform = platform.system()

if _platform == "Linux":
    class struct_AdapterInfo(Structure):
        __slots__ = [
            'iSize',
            'iAdapterIndex',
            'strUDID',
            'iBusNumber',
            'iDeviceNumber',
            'iFunctionNumber',
            'iVendorID',
            'strAdapterName',
            'strDisplayName',
            'iPresent',
            'iXScreenNum',
            'iDrvIndex',
            'strXScreenConfigName',
        ]
    struct_AdapterInfo._fields_ = [
        ('iSize', c_int),
        ('iAdapterIndex', c_int),
        ('strUDID', c_char * 256),
        ('iBusNumber', c_int),
        ('iDeviceNumber', c_int),
        ('iFunctionNumber', c_int),
        ('iVendorID', c_int),
        ('strAdapterName', c_char * 256),
        ('strDisplayName', c_char * 256),
        ('iPresent', c_int),
        ('iXScreenNum', c_int),
        ('iDrvIndex', c_int),
        ('strXScreenConfigName', c_char * 256),
    ]
elif _platform == "Windows":
    class struct_AdapterInfo(Structure):
        __slots__ = [
            'iSize',
            'iAdapterIndex',
            'strUDID',
            'iBusNumber',
            'iDeviceNumber',
            'iFunctionNumber',
            'iVendorID',
            'strAdapterName',
            'strDisplayName',
            'iPresent',
            'iExist',
            'strDriverPath',
            'strDriverPathExt',
            'strPNPString',
            'iOSDisplayIndex'
        ]
    struct_AdapterInfo._fields_ = [
        ('iSize', c_int),
        ('iAdapterIndex', c_int),
        ('strUDID', c_char * 256),
        ('iBusNumber', c_int),
        ('iDeviceNumber', c_int),
        ('iFunctionNumber', c_int),
        ('iVendorID', c_int),
        ('strAdapterName', c_char * 256),
        ('strDisplayName', c_char * 256),
        ('iPresent', c_int),
        ('iExist', c_int),
        ('strDriverPath', c_char * 256),
        ('strDriverPathExt', c_char * 256),
        ('strPNPString', c_char * 256),
        ('iOSDisplayIndex', c_int)
    ]

AdapterInfo = struct_AdapterInfo     # ADL_SDK_3.0/include/adl_structures.h:123
LPAdapterInfo = POINTER(struct_AdapterInfo)     # ADL_SDK_3.0/include/adl_structures.h:123
class struct_XScreenInfo(Structure):
    __slots__ = [
        'iXScreenNum',
        'strXScreenConfigName',
    ]
struct_XScreenInfo._fields_ = [
    ('iXScreenNum', c_int),
    ('strXScreenConfigName', c_char * 256),
]

XScreenInfo = struct_XScreenInfo     # ADL_SDK_3.0/include/adl_structures.h:152
LPXScreenInfo = POINTER(struct_XScreenInfo)     # ADL_SDK_3.0/include/adl_structures.h:152
class struct_ADLMemoryInfo(Structure):
    __slots__ = [
        'iMemorySize',
        'strMemoryType',
        'iMemoryBandwidth',
    ]
struct_ADLMemoryInfo._fields_ = [
    ('iMemorySize', c_longlong),
    ('strMemoryType', c_char * 256),
    ('iMemoryBandwidth', c_longlong),
]

ADLMemoryInfo = struct_ADLMemoryInfo     # ADL_SDK_3.0/include/adl_structures.h:181
LPADLMemoryInfo = POINTER(struct_ADLMemoryInfo)     # ADL_SDK_3.0/include/adl_structures.h:181
class struct_ADLDDCInfo(Structure):
    __slots__ = [
        'ulSize',
        'ulSupportsDDC',
        'ulManufacturerID',
        'ulProductID',
        'cDisplayName',
        'ulMaxHResolution',
        'ulMaxVResolution',
        'ulMaxRefresh',
        'ulPTMCx',
        'ulPTMCy',
        'ulPTMRefreshRate',
        'ulDDCInfoFlag',
    ]
struct_ADLDDCInfo._fields_ = [
    ('ulSize', c_int),
    ('ulSupportsDDC', c_int),
    ('ulManufacturerID', c_int),
    ('ulProductID', c_int),
    ('cDisplayName', c_char * 256),
    ('ulMaxHResolution', c_int),
    ('ulMaxVResolution', c_int),
    ('ulMaxRefresh', c_int),
    ('ulPTMCx', c_int),
    ('ulPTMCy', c_int),
    ('ulPTMRefreshRate', c_int),
    ('ulDDCInfoFlag', c_int),
]

ADLDDCInfo = struct_ADLDDCInfo     # ADL_SDK_3.0/include/adl_structures.h:235
LPADLDDCInfo = POINTER(struct_ADLDDCInfo)     # ADL_SDK_3.0/include/adl_structures.h:235
class struct_ADLGamma(Structure):
    __slots__ = [
        'fRed',
        'fGreen',
        'fBlue',
    ]
struct_ADLGamma._fields_ = [
    ('fRed', c_float),
    ('fGreen', c_float),
    ('fBlue', c_float),
]

ADLGamma = struct_ADLGamma     # ADL_SDK_3.0/include/adl_structures.h:264
LPADLGamma = POINTER(struct_ADLGamma)     # ADL_SDK_3.0/include/adl_structures.h:264
class struct_ADLCustomMode(Structure):
    __slots__ = [
        'iFlags',
        'iModeWidth',
        'iModeHeight',
        'iBaseModeWidth',
        'iBaseModeHeight',
        'iRefreshRate',
    ]
struct_ADLCustomMode._fields_ = [
    ('iFlags', c_int),
    ('iModeWidth', c_int),
    ('iModeHeight', c_int),
    ('iBaseModeWidth', c_int),
    ('iBaseModeHeight', c_int),
    ('iRefreshRate', c_int),
]

ADLCustomMode = struct_ADLCustomMode     # ADL_SDK_3.0/include/adl_structures.h:298
LPADLCustomMode = POINTER(struct_ADLCustomMode)     # ADL_SDK_3.0/include/adl_structures.h:298
class struct_ADLGetClocksOUT(Structure):
    __slots__ = [
        'ulHighCoreClock',
        'ulHighMemoryClock',
        'ulHighVddc',
        'ulCoreMin',
        'ulCoreMax',
        'ulMemoryMin',
        'ulMemoryMax',
        'ulActivityPercent',
        'ulCurrentCoreClock',
        'ulCurrentMemoryClock',
        'ulReserved',
    ]
struct_ADLGetClocksOUT._fields_ = [
    ('ulHighCoreClock', c_long),
    ('ulHighMemoryClock', c_long),
    ('ulHighVddc', c_long),
    ('ulCoreMin', c_long),
    ('ulCoreMax', c_long),
    ('ulMemoryMin', c_long),
    ('ulMemoryMax', c_long),
    ('ulActivityPercent', c_long),
    ('ulCurrentCoreClock', c_long),
    ('ulCurrentMemoryClock', c_long),
    ('ulReserved', c_long),
]

ADLGetClocksOUT = struct_ADLGetClocksOUT     # ADL_SDK_3.0/include/adl_structures.h:325
class struct_ADLDisplayConfig(Structure):
    __slots__ = [
        'ulSize',
        'ulConnectorType',
        'ulDeviceData',
        'ulOverridedDeviceData',
        'ulReserved',
    ]
struct_ADLDisplayConfig._fields_ = [
    ('ulSize', c_long),
    ('ulConnectorType', c_long),
    ('ulDeviceData', c_long),
    ('ulOverridedDeviceData', c_long),
    ('ulReserved', c_long),
]

ADLDisplayConfig = struct_ADLDisplayConfig     # ADL_SDK_3.0/include/adl_structures.h:356
class struct_ADLDisplayID(Structure):
    __slots__ = [
        'iDisplayLogicalIndex',
        'iDisplayPhysicalIndex',
        'iDisplayLogicalAdapterIndex',
        'iDisplayPhysicalAdapterIndex',
    ]
struct_ADLDisplayID._fields_ = [
    ('iDisplayLogicalIndex', c_int),
    ('iDisplayPhysicalIndex', c_int),
    ('iDisplayLogicalAdapterIndex', c_int),
    ('iDisplayPhysicalAdapterIndex', c_int),
]

ADLDisplayID = struct_ADLDisplayID     # ADL_SDK_3.0/include/adl_structures.h:408
LPADLDisplayID = POINTER(struct_ADLDisplayID)     # ADL_SDK_3.0/include/adl_structures.h:408
class struct_ADLDisplayInfo(Structure):
    __slots__ = [
        'displayID',
        'iDisplayControllerIndex',
        'strDisplayName',
        'strDisplayManufacturerName',
        'iDisplayType',
        'iDisplayOutputType',
        'iDisplayConnector',
        'iDisplayInfoMask',
        'iDisplayInfoValue',
    ]
struct_ADLDisplayInfo._fields_ = [
    ('displayID', ADLDisplayID),
    ('iDisplayControllerIndex', c_int),
    ('strDisplayName', c_char * 256),
    ('strDisplayManufacturerName', c_char * 256),
    ('iDisplayType', c_int),
    ('iDisplayOutputType', c_int),
    ('iDisplayConnector', c_int),
    ('iDisplayInfoMask', c_int),
    ('iDisplayInfoValue', c_int),
]

ADLDisplayInfo = struct_ADLDisplayInfo     # ADL_SDK_3.0/include/adl_structures.h:465
LPADLDisplayInfo = POINTER(struct_ADLDisplayInfo)     # ADL_SDK_3.0/include/adl_structures.h:465
class struct_ADLDisplayMode(Structure):
    __slots__ = [
        'iPelsHeight',
        'iPelsWidth',
        'iBitsPerPel',
        'iDisplayFrequency',
    ]
struct_ADLDisplayMode._fields_ = [
    ('iPelsHeight', c_int),
    ('iPelsWidth', c_int),
    ('iBitsPerPel', c_int),
    ('iDisplayFrequency', c_int),
]

ADLDisplayMode = struct_ADLDisplayMode     # ADL_SDK_3.0/include/adl_structures.h:495
class struct_ADLDetailedTiming(Structure):
    __slots__ = [
        'iSize',
        'sTimingFlags',
        'sHTotal',
        'sHDisplay',
        'sHSyncStart',
        'sHSyncWidth',
        'sVTotal',
        'sVDisplay',
        'sVSyncStart',
        'sVSyncWidth',
        'sPixelClock',
        'sHOverscanRight',
        'sHOverscanLeft',
        'sVOverscanBottom',
        'sVOverscanTop',
        'sOverscan8B',
        'sOverscanGR',
    ]
struct_ADLDetailedTiming._fields_ = [
    ('iSize', c_int),
    ('sTimingFlags', c_short),
    ('sHTotal', c_short),
    ('sHDisplay', c_short),
    ('sHSyncStart', c_short),
    ('sHSyncWidth', c_short),
    ('sVTotal', c_short),
    ('sVDisplay', c_short),
    ('sVSyncStart', c_short),
    ('sVSyncWidth', c_short),
    ('sPixelClock', c_short),
    ('sHOverscanRight', c_short),
    ('sHOverscanLeft', c_short),
    ('sVOverscanBottom', c_short),
    ('sVOverscanTop', c_short),
    ('sOverscan8B', c_short),
    ('sOverscanGR', c_short),
]

ADLDetailedTiming = struct_ADLDetailedTiming     # ADL_SDK_3.0/include/adl_structures.h:558
class struct_ADLDisplayModeInfo(Structure):
    __slots__ = [
        'iTimingStandard',
        'iPossibleStandard',
        'iRefreshRate',
        'iPelsWidth',
        'iPelsHeight',
        'sDetailedTiming',
    ]
struct_ADLDisplayModeInfo._fields_ = [
    ('iTimingStandard', c_int),
    ('iPossibleStandard', c_int),
    ('iRefreshRate', c_int),
    ('iPelsWidth', c_int),
    ('iPelsHeight', c_int),
    ('sDetailedTiming', ADLDetailedTiming),
]

ADLDisplayModeInfo = struct_ADLDisplayModeInfo     # ADL_SDK_3.0/include/adl_structures.h:592
class struct_ADLDisplayProperty(Structure):
    __slots__ = [
        'iSize',
        'iPropertyType',
        'iExpansionMode',
        'iSupport',
        'iCurrent',
        'iDefault',
    ]
struct_ADLDisplayProperty._fields_ = [
    ('iSize', c_int),
    ('iPropertyType', c_int),
    ('iExpansionMode', c_int),
    ('iSupport', c_int),
    ('iCurrent', c_int),
    ('iDefault', c_int),
]

ADLDisplayProperty = struct_ADLDisplayProperty     # ADL_SDK_3.0/include/adl_structures.h:626
class struct_ADLClockInfo(Structure):
    __slots__ = [
        'iCoreClock',
        'iMemoryClock',
    ]
struct_ADLClockInfo._fields_ = [
    ('iCoreClock', c_int),
    ('iMemoryClock', c_int),
]

ADLClockInfo = struct_ADLClockInfo     # ADL_SDK_3.0/include/adl_structures.h:650
LPADLClockInfo = POINTER(struct_ADLClockInfo)     # ADL_SDK_3.0/include/adl_structures.h:650
class struct_ADLI2C(Structure):
    __slots__ = [
        'iSize',
        'iLine',
        'iAddress',
        'iOffset',
        'iAction',
        'iSpeed',
        'iDataSize',
        'pcData',
    ]
struct_ADLI2C._fields_ = [
    ('iSize', c_int),
    ('iLine', c_int),
    ('iAddress', c_int),
    ('iOffset', c_int),
    ('iAction', c_int),
    ('iSpeed', c_int),
    ('iDataSize', c_int),
    ('pcData', c_char_p),
]

ADLI2C = struct_ADLI2C     # ADL_SDK_3.0/include/adl_structures.h:692
class struct_ADLDisplayEDIDData(Structure):
    __slots__ = [
        'iSize',
        'iFlag',
        'iEDIDSize',
        'iBlockIndex',
        'cEDIDData',
        'iReserved',
    ]
struct_ADLDisplayEDIDData._fields_ = [
    ('iSize', c_int),
    ('iFlag', c_int),
    ('iEDIDSize', c_int),
    ('iBlockIndex', c_int),
    ('cEDIDData', c_char * 256),
    ('iReserved', c_int * 4),
]

ADLDisplayEDIDData = struct_ADLDisplayEDIDData     # ADL_SDK_3.0/include/adl_structures.h:728
class struct_ADLControllerOverlayInput(Structure):
    __slots__ = [
        'iSize',
        'iOverlayAdjust',
        'iValue',
        'iReserved',
    ]
struct_ADLControllerOverlayInput._fields_ = [
    ('iSize', c_int),
    ('iOverlayAdjust', c_int),
    ('iValue', c_int),
    ('iReserved', c_int),
]

ADLControllerOverlayInput = struct_ADLControllerOverlayInput     # ADL_SDK_3.0/include/adl_structures.h:760
class struct_ADLAdjustmentinfo(Structure):
    __slots__ = [
        'iDefault',
        'iMin',
        'iMax',
        'iStep',
    ]
struct_ADLAdjustmentinfo._fields_ = [
    ('iDefault', c_int),
    ('iMin', c_int),
    ('iMax', c_int),
    ('iStep', c_int),
]

ADLAdjustmentinfo = struct_ADLAdjustmentinfo     # ADL_SDK_3.0/include/adl_structures.h:790
class struct_ADLControllerOverlayInfo(Structure):
    __slots__ = [
        'iSize',
        'sOverlayInfo',
        'iReserved',
    ]
struct_ADLControllerOverlayInfo._fields_ = [
    ('iSize', c_int),
    ('sOverlayInfo', ADLAdjustmentinfo),
    ('iReserved', c_int * 3),
]

ADLControllerOverlayInfo = struct_ADLControllerOverlayInfo     # ADL_SDK_3.0/include/adl_structures.h:817
class struct_ADLGLSyncModuleID(Structure):
    __slots__ = [
        'iModuleID',
        'iGlSyncGPUPort',
        'iFWBootSectorVersion',
        'iFWUserSectorVersion',
    ]
struct_ADLGLSyncModuleID._fields_ = [
    ('iModuleID', c_int),
    ('iGlSyncGPUPort', c_int),
    ('iFWBootSectorVersion', c_int),
    ('iFWUserSectorVersion', c_int),
]

ADLGLSyncModuleID = struct_ADLGLSyncModuleID     # ADL_SDK_3.0/include/adl_structures.h:847
LPADLGLSyncModuleID = POINTER(struct_ADLGLSyncModuleID)     # ADL_SDK_3.0/include/adl_structures.h:847
class struct_ADLGLSyncPortCaps(Structure):
    __slots__ = [
        'iPortType',
        'iNumOfLEDs',
    ]
struct_ADLGLSyncPortCaps._fields_ = [
    ('iPortType', c_int),
    ('iNumOfLEDs', c_int),
]

ADLGLSyncPortCaps = struct_ADLGLSyncPortCaps     # ADL_SDK_3.0/include/adl_structures.h:871
LPADLGLSyncPortCaps = POINTER(struct_ADLGLSyncPortCaps)     # ADL_SDK_3.0/include/adl_structures.h:871
class struct_ADLGLSyncGenlockConfig(Structure):
    __slots__ = [
        'iValidMask',
        'iSyncDelay',
        'iFramelockCntlVector',
        'iSignalSource',
        'iSampleRate',
        'iSyncField',
        'iTriggerEdge',
        'iScanRateCoeff',
    ]
struct_ADLGLSyncGenlockConfig._fields_ = [
    ('iValidMask', c_int),
    ('iSyncDelay', c_int),
    ('iFramelockCntlVector', c_int),
    ('iSignalSource', c_int),
    ('iSampleRate', c_int),
    ('iSyncField', c_int),
    ('iTriggerEdge', c_int),
    ('iScanRateCoeff', c_int),
]

ADLGLSyncGenlockConfig = struct_ADLGLSyncGenlockConfig     # ADL_SDK_3.0/include/adl_structures.h:915
LPADLGLSyncGenlockConfig = POINTER(struct_ADLGLSyncGenlockConfig)     # ADL_SDK_3.0/include/adl_structures.h:915
class struct_ADLGlSyncPortInfo(Structure):
    __slots__ = [
        'iPortType',
        'iNumOfLEDs',
        'iPortState',
        'iFrequency',
        'iSignalType',
        'iSignalSource',
    ]
struct_ADLGlSyncPortInfo._fields_ = [
    ('iPortType', c_int),
    ('iNumOfLEDs', c_int),
    ('iPortState', c_int),
    ('iFrequency', c_int),
    ('iSignalType', c_int),
    ('iSignalSource', c_int),
]

ADLGlSyncPortInfo = struct_ADLGlSyncPortInfo     # ADL_SDK_3.0/include/adl_structures.h:954
LPADLGlSyncPortInfo = POINTER(struct_ADLGlSyncPortInfo)     # ADL_SDK_3.0/include/adl_structures.h:954
class struct_ADLGlSyncPortControl(Structure):
    __slots__ = [
        'iPortType',
        'iControlVector',
        'iSignalSource',
    ]
struct_ADLGlSyncPortControl._fields_ = [
    ('iPortType', c_int),
    ('iControlVector', c_int),
    ('iSignalSource', c_int),
]

ADLGlSyncPortControl = struct_ADLGlSyncPortControl     # ADL_SDK_3.0/include/adl_structures.h:983
class struct_ADLGlSyncMode(Structure):
    __slots__ = [
        'iControlVector',
        'iStatusVector',
        'iGLSyncConnectorIndex',
    ]
struct_ADLGlSyncMode._fields_ = [
    ('iControlVector', c_int),
    ('iStatusVector', c_int),
    ('iGLSyncConnectorIndex', c_int),
]

ADLGlSyncMode = struct_ADLGlSyncMode     # ADL_SDK_3.0/include/adl_structures.h:1012
LPADLGlSyncMode = POINTER(struct_ADLGlSyncMode)     # ADL_SDK_3.0/include/adl_structures.h:1012
class struct_ADLGlSyncMode2(Structure):
    __slots__ = [
        'iControlVector',
        'iStatusVector',
        'iGLSyncConnectorIndex',
        'iDisplayIndex',
    ]
struct_ADLGlSyncMode2._fields_ = [
    ('iControlVector', c_int),
    ('iStatusVector', c_int),
    ('iGLSyncConnectorIndex', c_int),
    ('iDisplayIndex', c_int),
]

ADLGlSyncMode2 = struct_ADLGlSyncMode2     # ADL_SDK_3.0/include/adl_structures.h:1044
LPADLGlSyncMode2 = POINTER(struct_ADLGlSyncMode2)     # ADL_SDK_3.0/include/adl_structures.h:1044
class struct_ADLInfoPacket(Structure):
    __slots__ = [
        'hb0',
        'hb1',
        'hb2',
        'sb',
    ]
struct_ADLInfoPacket._fields_ = [
    ('hb0', c_char),
    ('hb1', c_char),
    ('hb2', c_char),
    ('sb', c_char * 28),
]

ADLInfoPacket = struct_ADLInfoPacket     # ADL_SDK_3.0/include/adl_structures.h:1069
class struct_ADLAVIInfoPacket(Structure):
    __slots__ = [
        'bPB3_ITC',
        'bPB5',
    ]
struct_ADLAVIInfoPacket._fields_ = [
    ('bPB3_ITC', c_char),
    ('bPB5', c_char),
]

ADLAVIInfoPacket = struct_ADLAVIInfoPacket     # ADL_SDK_3.0/include/adl_structures.h:1094
class struct_ADLODClockSetting(Structure):
    __slots__ = [
        'iDefaultClock',
        'iCurrentClock',
        'iMaxClock',
        'iMinClock',
        'iRequestedClock',
        'iStepClock',
    ]
struct_ADLODClockSetting._fields_ = [
    ('iDefaultClock', c_int),
    ('iCurrentClock', c_int),
    ('iMaxClock', c_int),
    ('iMinClock', c_int),
    ('iRequestedClock', c_int),
    ('iStepClock', c_int),
]

ADLODClockSetting = struct_ADLODClockSetting     # ADL_SDK_3.0/include/adl_structures.h:1133
class struct_ADLAdapterODClockInfo(Structure):
    __slots__ = [
        'iSize',
        'iFlags',
        'sMemoryClock',
        'sEngineClock',
    ]
struct_ADLAdapterODClockInfo._fields_ = [
    ('iSize', c_int),
    ('iFlags', c_int),
    ('sMemoryClock', ADLODClockSetting),
    ('sEngineClock', ADLODClockSetting),
]

ADLAdapterODClockInfo = struct_ADLAdapterODClockInfo     # ADL_SDK_3.0/include/adl_structures.h:1163
class struct_ADLAdapterODClockConfig(Structure):
    __slots__ = [
        'iSize',
        'iFlags',
        'iMemoryClock',
        'iEngineClock',
    ]
struct_ADLAdapterODClockConfig._fields_ = [
    ('iSize', c_int),
    ('iFlags', c_int),
    ('iMemoryClock', c_int),
    ('iEngineClock', c_int),
]

ADLAdapterODClockConfig = struct_ADLAdapterODClockConfig     # ADL_SDK_3.0/include/adl_structures.h:1193
class struct_ADLPMActivity(Structure):
    __slots__ = [
        'iSize',
        'iEngineClock',
        'iMemoryClock',
        'iVddc',
        'iActivityPercent',
        'iCurrentPerformanceLevel',
        'iCurrentBusSpeed',
        'iCurrentBusLanes',
        'iMaximumBusLanes',
        'iReserved',
    ]
struct_ADLPMActivity._fields_ = [
    ('iSize', c_int),
    ('iEngineClock', c_int),
    ('iMemoryClock', c_int),
    ('iVddc', c_int),
    ('iActivityPercent', c_int),
    ('iCurrentPerformanceLevel', c_int),
    ('iCurrentBusSpeed', c_int),
    ('iCurrentBusLanes', c_int),
    ('iMaximumBusLanes', c_int),
    ('iReserved', c_int),
]

ADLPMActivity = struct_ADLPMActivity     # ADL_SDK_3.0/include/adl_structures.h:1241
class struct_ADLThermalControllerInfo(Structure):
    __slots__ = [
        'iSize',
        'iThermalDomain',
        'iDomainIndex',
        'iFlags',
    ]
struct_ADLThermalControllerInfo._fields_ = [
    ('iSize', c_int),
    ('iThermalDomain', c_int),
    ('iDomainIndex', c_int),
    ('iFlags', c_int),
]

ADLThermalControllerInfo = struct_ADLThermalControllerInfo     # ADL_SDK_3.0/include/adl_structures.h:1271
class struct_ADLTemperature(Structure):
    __slots__ = [
        'iSize',
        'iTemperature',
    ]
struct_ADLTemperature._fields_ = [
    ('iSize', c_int),
    ('iTemperature', c_int),
]

ADLTemperature = struct_ADLTemperature     # ADL_SDK_3.0/include/adl_structures.h:1295
class struct_ADLFanSpeedInfo(Structure):
    __slots__ = [
        'iSize',
        'iFlags',
        'iMinPercent',
        'iMaxPercent',
        'iMinRPM',
        'iMaxRPM',
    ]
struct_ADLFanSpeedInfo._fields_ = [
    ('iSize', c_int),
    ('iFlags', c_int),
    ('iMinPercent', c_int),
    ('iMaxPercent', c_int),
    ('iMinRPM', c_int),
    ('iMaxRPM', c_int),
]

ADLFanSpeedInfo = struct_ADLFanSpeedInfo     # ADL_SDK_3.0/include/adl_structures.h:1331
class struct_ADLFanSpeedValue(Structure):
    __slots__ = [
        'iSize',
        'iSpeedType',
        'iFanSpeed',
        'iFlags',
    ]
struct_ADLFanSpeedValue._fields_ = [
    ('iSize', c_int),
    ('iSpeedType', c_int),
    ('iFanSpeed', c_int),
    ('iFlags', c_int),
]

ADLFanSpeedValue = struct_ADLFanSpeedValue     # ADL_SDK_3.0/include/adl_structures.h:1361
class struct_ADLODParameterRange(Structure):
    __slots__ = [
        'iMin',
        'iMax',
        'iStep',
    ]
struct_ADLODParameterRange._fields_ = [
    ('iMin', c_int),
    ('iMax', c_int),
    ('iStep', c_int),
]

ADLODParameterRange = struct_ADLODParameterRange     # ADL_SDK_3.0/include/adl_structures.h:1388
class struct_ADLODParameters(Structure):
    __slots__ = [
        'iSize',
        'iNumberOfPerformanceLevels',
        'iActivityReportingSupported',
        'iDiscretePerformanceLevels',
        'iReserved',
        'sEngineClock',
        'sMemoryClock',
        'sVddc',
    ]
struct_ADLODParameters._fields_ = [
    ('iSize', c_int),
    ('iNumberOfPerformanceLevels', c_int),
    ('iActivityReportingSupported', c_int),
    ('iDiscretePerformanceLevels', c_int),
    ('iReserved', c_int),
    ('sEngineClock', ADLODParameterRange),
    ('sMemoryClock', ADLODParameterRange),
    ('sVddc', ADLODParameterRange),
]

ADLODParameters = struct_ADLODParameters     # ADL_SDK_3.0/include/adl_structures.h:1430
class struct_ADLODPerformanceLevel(Structure):
    __slots__ = [
        'iEngineClock',
        'iMemoryClock',
        'iVddc',
    ]
struct_ADLODPerformanceLevel._fields_ = [
    ('iEngineClock', c_int),
    ('iMemoryClock', c_int),
    ('iVddc', c_int),
]

ADLODPerformanceLevel = struct_ADLODPerformanceLevel     # ADL_SDK_3.0/include/adl_structures.h:1457
class struct_ADLODPerformanceLevels(Structure):
    __slots__ = [
        'iSize',
        'iReserved',
        'aLevels',
    ]
struct_ADLODPerformanceLevels._fields_ = [
    ('iSize', c_int),
    ('iReserved', c_int),
    ('aLevels', ADLODPerformanceLevel * 1),
]

ADLODPerformanceLevels = struct_ADLODPerformanceLevels     # ADL_SDK_3.0/include/adl_structures.h:1482
class struct_ADLCrossfireComb(Structure):
    __slots__ = [
        'iNumLinkAdapter',
        'iAdaptLink',
    ]
struct_ADLCrossfireComb._fields_ = [
    ('iNumLinkAdapter', c_int),
    ('iAdaptLink', c_int * 3),
]

ADLCrossfireComb = struct_ADLCrossfireComb     # ADL_SDK_3.0/include/adl_structures.h:1506
class struct_ADLCrossfireInfo(Structure):
    __slots__ = [
        'iErrorCode',
        'iState',
        'iSupported',
    ]
struct_ADLCrossfireInfo._fields_ = [
    ('iErrorCode', c_int),
    ('iState', c_int),
    ('iSupported', c_int),
]

ADLCrossfireInfo = struct_ADLCrossfireInfo     # ADL_SDK_3.0/include/adl_structures.h:1533
class struct_ADLBiosInfo(Structure):
    __slots__ = [
        'strPartNumber',
        'strVersion',
        'strDate',
    ]
struct_ADLBiosInfo._fields_ = [
    ('strPartNumber', c_char * 256),
    ('strVersion', c_char * 256),
    ('strDate', c_char * 256),
]

ADLBiosInfo = struct_ADLBiosInfo     # ADL_SDK_3.0/include/adl_structures.h:1557
LPADLBiosInfo = POINTER(struct_ADLBiosInfo)     # ADL_SDK_3.0/include/adl_structures.h:1557
class struct_ADLAdapterLocation(Structure):
    __slots__ = [
        'iBus',
        'iDevice',
        'iFunction',
    ]
struct_ADLAdapterLocation._fields_ = [
    ('iBus', c_int),
    ('iDevice', c_int),
    ('iFunction', c_int),
]

ADLAdapterLocation = struct_ADLAdapterLocation     # ADL_SDK_3.0/include/adl_structures.h:1585
class struct_ADLMVPUCaps(Structure):
    __slots__ = [
        'iSize',
        'iAdapterCount',
        'iPossibleMVPUMasters',
        'iPossibleMVPUSlaves',
        'cAdapterPath',
    ]
struct_ADLMVPUCaps._fields_ = [
    ('iSize', c_int),
    ('iAdapterCount', c_int),
    ('iPossibleMVPUMasters', c_int),
    ('iPossibleMVPUSlaves', c_int),
    ('cAdapterPath', (c_char * 256) * 4),
]

ADLMVPUCaps = struct_ADLMVPUCaps     # ADL_SDK_3.0/include/adl_structures.h:1618
class struct_ADLMVPUStatus(Structure):
    __slots__ = [
        'iSize',
        'iActiveAdapterCount',
        'iStatus',
        'aAdapterLocation',
    ]
struct_ADLMVPUStatus._fields_ = [
    ('iSize', c_int),
    ('iActiveAdapterCount', c_int),
    ('iStatus', c_int),
    ('aAdapterLocation', ADLAdapterLocation * 4),
]

ADLMVPUStatus = struct_ADLMVPUStatus     # ADL_SDK_3.0/include/adl_structures.h:1648
class struct_ADLActivatableSource(Structure):
    __slots__ = [
        'iAdapterIndex',
        'iNumActivatableSources',
        'iActivatableSourceMask',
        'iActivatableSourceValue',
    ]
struct_ADLActivatableSource._fields_ = [
    ('iAdapterIndex', c_int),
    ('iNumActivatableSources', c_int),
    ('iActivatableSourceMask', c_int),
    ('iActivatableSourceValue', c_int),
]

ADLActivatableSource = struct_ADLActivatableSource     # ADL_SDK_3.0/include/adl_structures.h:1681
LPADLActivatableSource = POINTER(struct_ADLActivatableSource)     # ADL_SDK_3.0/include/adl_structures.h:1681
class struct_ADLMode(Structure):
    __slots__ = [
        'iAdapterIndex',
        'displayID',
        'iXPos',
        'iYPos',
        'iXRes',
        'iYRes',
        'iColourDepth',
        'fRefreshRate',
        'iOrientation',
        'iModeFlag',
        'iModeMask',
        'iModeValue',
    ]
struct_ADLMode._fields_ = [
    ('iAdapterIndex', c_int),
    ('displayID', ADLDisplayID),
    ('iXPos', c_int),
    ('iYPos', c_int),
    ('iXRes', c_int),
    ('iYRes', c_int),
    ('iColourDepth', c_int),
    ('fRefreshRate', c_float),
    ('iOrientation', c_int),
    ('iModeFlag', c_int),
    ('iModeMask', c_int),
    ('iModeValue', c_int),
]

ADLMode = struct_ADLMode     # ADL_SDK_3.0/include/adl_structures.h:1738
LPADLMode = POINTER(struct_ADLMode)     # ADL_SDK_3.0/include/adl_structures.h:1738
class struct_ADLDisplayTarget(Structure):
    __slots__ = [
        'displayID',
        'iDisplayMapIndex',
        'iDisplayTargetMask',
        'iDisplayTargetValue',
    ]
struct_ADLDisplayTarget._fields_ = [
    ('displayID', ADLDisplayID),
    ('iDisplayMapIndex', c_int),
    ('iDisplayTargetMask', c_int),
    ('iDisplayTargetValue', c_int),
]

ADLDisplayTarget = struct_ADLDisplayTarget     # ADL_SDK_3.0/include/adl_structures.h:1771
LPADLDisplayTarget = POINTER(struct_ADLDisplayTarget)     # ADL_SDK_3.0/include/adl_structures.h:1771
class struct_tagADLBezelTransientMode(Structure):
    __slots__ = [
        'iAdapterIndex',
        'iSLSMapIndex',
        'iSLSModeIndex',
        'displayMode',
        'iNumBezelOffset',
        'iFirstBezelOffsetArrayIndex',
        'iSLSBezelTransientModeMask',
        'iSLSBezelTransientModeValue',
    ]
struct_tagADLBezelTransientMode._fields_ = [
    ('iAdapterIndex', c_int),
    ('iSLSMapIndex', c_int),
    ('iSLSModeIndex', c_int),
    ('displayMode', ADLMode),
    ('iNumBezelOffset', c_int),
    ('iFirstBezelOffsetArrayIndex', c_int),
    ('iSLSBezelTransientModeMask', c_int),
    ('iSLSBezelTransientModeValue', c_int),
]

ADLBezelTransientMode = struct_tagADLBezelTransientMode     # ADL_SDK_3.0/include/adl_structures.h:1820
LPADLBezelTransientMode = POINTER(struct_tagADLBezelTransientMode)     # ADL_SDK_3.0/include/adl_structures.h:1820
class struct_ADLAdapterDisplayCap(Structure):
    __slots__ = [
        'iAdapterIndex',
        'iAdapterDisplayCapMask',
        'iAdapterDisplayCapValue',
    ]
struct_ADLAdapterDisplayCap._fields_ = [
    ('iAdapterIndex', c_int),
    ('iAdapterDisplayCapMask', c_int),
    ('iAdapterDisplayCapValue', c_int),
]

ADLAdapterDisplayCap = struct_ADLAdapterDisplayCap     # ADL_SDK_3.0/include/adl_structures.h:1850
LPADLAdapterDisplayCap = POINTER(struct_ADLAdapterDisplayCap)     # ADL_SDK_3.0/include/adl_structures.h:1850
class struct_ADLDisplayMap(Structure):
    __slots__ = [
        'iDisplayMapIndex',
        'displayMode',
        'iNumDisplayTarget',
        'iFirstDisplayTargetArrayIndex',
        'iDisplayMapMask',
        'iDisplayMapValue',
    ]
struct_ADLDisplayMap._fields_ = [
    ('iDisplayMapIndex', c_int),
    ('displayMode', ADLMode),
    ('iNumDisplayTarget', c_int),
    ('iFirstDisplayTargetArrayIndex', c_int),
    ('iDisplayMapMask', c_int),
    ('iDisplayMapValue', c_int),
]

ADLDisplayMap = struct_ADLDisplayMap     # ADL_SDK_3.0/include/adl_structures.h:1895
LPADLDisplayMap = POINTER(struct_ADLDisplayMap)     # ADL_SDK_3.0/include/adl_structures.h:1895
class struct_ADLPossibleMap(Structure):
    __slots__ = [
        'iIndex',
        'iAdapterIndex',
        'iNumDisplayMap',
        'displayMap',
        'iNumDisplayTarget',
        'displayTarget',
    ]
struct_ADLPossibleMap._fields_ = [
    ('iIndex', c_int),
    ('iAdapterIndex', c_int),
    ('iNumDisplayMap', c_int),
    ('displayMap', POINTER(ADLDisplayMap)),
    ('iNumDisplayTarget', c_int),
    ('displayTarget', POINTER(ADLDisplayTarget)),
]

ADLPossibleMap = struct_ADLPossibleMap     # ADL_SDK_3.0/include/adl_structures.h:1932
LPADLPossibleMap = POINTER(struct_ADLPossibleMap)     # ADL_SDK_3.0/include/adl_structures.h:1932
class struct_ADLPossibleMapping(Structure):
    __slots__ = [
        'iDisplayIndex',
        'iDisplayControllerIndex',
        'iDisplayMannerSupported',
    ]
struct_ADLPossibleMapping._fields_ = [
    ('iDisplayIndex', c_int),
    ('iDisplayControllerIndex', c_int),
    ('iDisplayMannerSupported', c_int),
]

ADLPossibleMapping = struct_ADLPossibleMapping     # ADL_SDK_3.0/include/adl_structures.h:1955
LPADLPossibleMapping = POINTER(struct_ADLPossibleMapping)     # ADL_SDK_3.0/include/adl_structures.h:1955
class struct_ADLPossibleMapResult(Structure):
    __slots__ = [
        'iIndex',
        'iPossibleMapResultMask',
        'iPossibleMapResultValue',
    ]
struct_ADLPossibleMapResult._fields_ = [
    ('iIndex', c_int),
    ('iPossibleMapResultMask', c_int),
    ('iPossibleMapResultValue', c_int),
]

ADLPossibleMapResult = struct_ADLPossibleMapResult     # ADL_SDK_3.0/include/adl_structures.h:1982
LPADLPossibleMapResult = POINTER(struct_ADLPossibleMapResult)     # ADL_SDK_3.0/include/adl_structures.h:1982
class struct_ADLSLSGrid(Structure):
    __slots__ = [
        'iAdapterIndex',
        'iSLSGridIndex',
        'iSLSGridRow',
        'iSLSGridColumn',
        'iSLSGridMask',
        'iSLSGridValue',
    ]
struct_ADLSLSGrid._fields_ = [
    ('iAdapterIndex', c_int),
    ('iSLSGridIndex', c_int),
    ('iSLSGridRow', c_int),
    ('iSLSGridColumn', c_int),
    ('iSLSGridMask', c_int),
    ('iSLSGridValue', c_int),
]

ADLSLSGrid = struct_ADLSLSGrid     # ADL_SDK_3.0/include/adl_structures.h:2022
LPADLSLSGrid = POINTER(struct_ADLSLSGrid)     # ADL_SDK_3.0/include/adl_structures.h:2022
class struct_ADLSLSMap(Structure):
    __slots__ = [
        'iAdapterIndex',
        'iSLSMapIndex',
        'grid',
        'iSurfaceMapIndex',
        'iOrientation',
        'iNumSLSTarget',
        'iFirstSLSTargetArrayIndex',
        'iNumNativeMode',
        'iFirstNativeModeArrayIndex',
        'iNumBezelMode',
        'iFirstBezelModeArrayIndex',
        'iNumBezelOffset',
        'iFirstBezelOffsetArrayIndex',
        'iSLSMapMask',
        'iSLSMapValue',
    ]
struct_ADLSLSMap._fields_ = [
    ('iAdapterIndex', c_int),
    ('iSLSMapIndex', c_int),
    ('grid', ADLSLSGrid),
    ('iSurfaceMapIndex', c_int),
    ('iOrientation', c_int),
    ('iNumSLSTarget', c_int),
    ('iFirstSLSTargetArrayIndex', c_int),
    ('iNumNativeMode', c_int),
    ('iFirstNativeModeArrayIndex', c_int),
    ('iNumBezelMode', c_int),
    ('iFirstBezelModeArrayIndex', c_int),
    ('iNumBezelOffset', c_int),
    ('iFirstBezelOffsetArrayIndex', c_int),
    ('iSLSMapMask', c_int),
    ('iSLSMapValue', c_int),
]

ADLSLSMap = struct_ADLSLSMap     # ADL_SDK_3.0/include/adl_structures.h:2099
LPADLSLSMap = POINTER(struct_ADLSLSMap)     # ADL_SDK_3.0/include/adl_structures.h:2099
class struct_ADLSLSOffset(Structure):
    __slots__ = [
        'iAdapterIndex',
        'iSLSMapIndex',
        'displayID',
        'iBezelModeIndex',
        'iBezelOffsetX',
        'iBezelOffsetY',
        'iDisplayWidth',
        'iDisplayHeight',
        'iBezelOffsetMask',
        'iBezelffsetValue',
    ]
struct_ADLSLSOffset._fields_ = [
    ('iAdapterIndex', c_int),
    ('iSLSMapIndex', c_int),
    ('displayID', ADLDisplayID),
    ('iBezelModeIndex', c_int),
    ('iBezelOffsetX', c_int),
    ('iBezelOffsetY', c_int),
    ('iDisplayWidth', c_int),
    ('iDisplayHeight', c_int),
    ('iBezelOffsetMask', c_int),
    ('iBezelffsetValue', c_int),
]

ADLSLSOffset = struct_ADLSLSOffset     # ADL_SDK_3.0/include/adl_structures.h:2154
LPADLSLSOffset = POINTER(struct_ADLSLSOffset)     # ADL_SDK_3.0/include/adl_structures.h:2154
class struct_ADLSLSMode(Structure):
    __slots__ = [
        'iAdapterIndex',
        'iSLSMapIndex',
        'iSLSModeIndex',
        'displayMode',
        'iSLSNativeModeMask',
        'iSLSNativeModeValue',
    ]
struct_ADLSLSMode._fields_ = [
    ('iAdapterIndex', c_int),
    ('iSLSMapIndex', c_int),
    ('iSLSModeIndex', c_int),
    ('displayMode', ADLMode),
    ('iSLSNativeModeMask', c_int),
    ('iSLSNativeModeValue', c_int),
]

ADLSLSMode = struct_ADLSLSMode     # ADL_SDK_3.0/include/adl_structures.h:2193
LPADLSLSMode = POINTER(struct_ADLSLSMode)     # ADL_SDK_3.0/include/adl_structures.h:2193
class struct_ADLPossibleSLSMap(Structure):
    __slots__ = [
        'iSLSMapIndex',
        'iNumSLSMap',
        'lpSLSMap',
        'iNumSLSTarget',
        'lpDisplayTarget',
    ]
struct_ADLPossibleSLSMap._fields_ = [
    ('iSLSMapIndex', c_int),
    ('iNumSLSMap', c_int),
    ('lpSLSMap', POINTER(ADLSLSMap)),
    ('iNumSLSTarget', c_int),
    ('lpDisplayTarget', POINTER(ADLDisplayTarget)),
]

ADLPossibleSLSMap = struct_ADLPossibleSLSMap     # ADL_SDK_3.0/include/adl_structures.h:2233
LPADLPossibleSLSMap = POINTER(struct_ADLPossibleSLSMap)     # ADL_SDK_3.0/include/adl_structures.h:2233
class struct_ADLSLSTarget(Structure):
    __slots__ = [
        'iAdapterIndex',
        'iSLSMapIndex',
        'displayTarget',
        'iSLSGridPositionX',
        'iSLSGridPositionY',
        'viewSize',
        'iSLSTargetMask',
        'iSLSTargetValue',
    ]
struct_ADLSLSTarget._fields_ = [
    ('iAdapterIndex', c_int),
    ('iSLSMapIndex', c_int),
    ('displayTarget', ADLDisplayTarget),
    ('iSLSGridPositionX', c_int),
    ('iSLSGridPositionY', c_int),
    ('viewSize', ADLMode),
    ('iSLSTargetMask', c_int),
    ('iSLSTargetValue', c_int),
]

ADLSLSTarget = struct_ADLSLSTarget     # ADL_SDK_3.0/include/adl_structures.h:2282
LPADLSLSTarget = POINTER(struct_ADLSLSTarget)     # ADL_SDK_3.0/include/adl_structures.h:2282
class struct_ADLBezelOffsetSteppingSize(Structure):
    __slots__ = [
        'iAdapterIndex',
        'iSLSMapIndex',
        'iBezelOffsetSteppingSizeX',
        'iBezelOffsetSteppingSizeY',
        'iBezelOffsetSteppingSizeMask',
        'iBezelOffsetSteppingSizeValue',
    ]
struct_ADLBezelOffsetSteppingSize._fields_ = [
    ('iAdapterIndex', c_int),
    ('iSLSMapIndex', c_int),
    ('iBezelOffsetSteppingSizeX', c_int),
    ('iBezelOffsetSteppingSizeY', c_int),
    ('iBezelOffsetSteppingSizeMask', c_int),
    ('iBezelOffsetSteppingSizeValue', c_int),
]

ADLBezelOffsetSteppingSize = struct_ADLBezelOffsetSteppingSize     # ADL_SDK_3.0/include/adl_structures.h:2322
LPADLBezelOffsetSteppingSize = POINTER(struct_ADLBezelOffsetSteppingSize)     # ADL_SDK_3.0/include/adl_structures.h:2322
