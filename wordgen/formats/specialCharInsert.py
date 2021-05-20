# Copyright 2021 Alex Zhao
#
# This file is part of WordGen.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
# insert special char format
def main(fstr, config, usedKeywords):
    """insert special char format
    - interable"""
    result = []
    words = usedKeywords[:]
    for i in config.get('specialChar'):
        for index in range(len(words)+1):
            words.insert(index, i)
            result.append(''.join(words))
            words.pop(index)
    return result