# rebuildd - Debian packages rebuild tool 
# 
# (c) 2007 - Julien Danjou <acid@debian.org> 
# 
#   This software is free software; you can redistribute it and/or modify 
#   it under the terms of the GNU General Public License as published by 
#   the Free Software Foundation; version 2 dated June, 1991. 
# 
#   This software is distributed in the hope that it will be useful, 
#   but WITHOUT ANY WARRANTY; without even the implied warranty of 
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
#   GNU General Public License for more details. 
# 
#   You should have received a copy of the GNU General Public License 
#   along with this software; if not, write to the Free Software 
#   Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA 
# 

from Enumeration import Enumeration

JobStatus = Enumeration([ ("UNKNOWN", 0), 
                          ("WAIT", 100), 
                          ("WAIT_LOCKED", 150),
                          ("BUILDING", 200), 
                          ("SOURCE_FAILED", 250), 
                          ("BUILD_FAILED", 300), 
                          ("POST_BUILD_FAILED", 350), 
                          ("CANCELED", 800), 
                          ("GIVEUP", 850),
                          ("FAILED", 900),
                          ("BUILD_OK", 1000) ])

FailedStatus = (JobStatus.SOURCE_FAILED,
                JobStatus.BUILD_FAILED,
                JobStatus.POST_BUILD_FAILED)
