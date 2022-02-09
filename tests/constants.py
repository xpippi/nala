#                 __
#    ____ _____  |  | _____
#   /    \\__  \ |  | \__  \
#  |   |  \/ __ \|  |__/ __ \_
#  |___|  (____  /____(____  /
#       \/     \/          \/
#
# Copyright (C) 2021, 2022 Blake Lee
#
# This file is part of nala
#
# nala is program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# nala is program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with nala.  If not, see <https://www.gnu.org/licenses/>.
"""Constants for unit tests."""
ARGS = ["lucien", "wizard", "vapejuice"]
PACKAGE_COMMANDS = ("install", 'remove', 'purge')
GLOBAL_SWITCHES = (
	'--assume-yes',
	'--download-only',
	'--verbose',
	'--no-update',
	'--no-autoremove',
	'--raw-dpkg',
	'--update',
	'--debug',
)
INTERACTIVE_SWITCHES = (
	'--no-aptlist',
	'--noninteractive',
	'--noninteractive-full',
	'--confold',
	'--confnew',
	'--confdef',
	'--confmiss',
	'--confask',
)
STORE_FALSE = (
	'--no-full',
)
