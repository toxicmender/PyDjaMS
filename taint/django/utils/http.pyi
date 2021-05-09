# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-unsafe

from typing import Any, Mapping, Optional

def int_to_base36(i: int) -> str: ...
def base36_to_int(s: str) -> int: ...
def urlencode(data: Mapping[str, Any], doseq: bool = ...) -> str: ...
def urlquote(url: str, safe: str = ...) -> str: ...
def http_date(epoch_seconds: Optional[float] = None) -> str: ...
def same_origin(lhs: str, rhs: str) -> bool: ...
def is_safe_url(url: str, host: Optional[str] = None) -> bool: ...
