#! /usr/bin/python
# coding: UTF-8
import sys
l1_opy_ = sys.version_info [0] == 2
l11_opy_ = 2048
l1l11_opy_ = 7
def l1lll_opy_ (ll_opy_):
    global l1l_opy_
    l1l1l_opy_ = ord (ll_opy_ [-1])
    l1ll1_opy_ = ll_opy_ [:-1]
    l1l1_opy_ = l1l1l_opy_ % len (l1ll1_opy_)
    l11l_opy_ = l1ll1_opy_ [:l1l1_opy_] + l1ll1_opy_ [l1l1_opy_:]
    if l1_opy_:
        l1ll_opy_ = unicode () .join ([unichr (ord (char) - l11_opy_ - (l111_opy_ + l1l1l_opy_) % l1l11_opy_) for l111_opy_, char in enumerate (l11l_opy_)])
    else:
        l1ll_opy_ = str () .join ([chr (ord (char) - l11_opy_ - (l111_opy_ + l1l1l_opy_) % l1l11_opy_) for l111_opy_, char in enumerate (l11l_opy_)])
    return eval (l1ll_opy_)
license = (
'''Copyright 2014, 2015, 2016, 2017 Jacques de Hooge, GEATEC engineering, www.geatec.com
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''
)
import re
import os
import sys
import errno
import keyword
import importlib
import random
import codecs
import shutil
l11l1l1_opy_ = l1lll_opy_ (u"ࠫࡴࡶࡹࠨࠀ")
l1lll1_opy_ = l1lll_opy_ (u"ࠬ࠷࠮࠲࠰࠵࠸ࠬࠁ")
if __name__ == l1lll_opy_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨࠂ"):
    print (l1lll_opy_ (u"ࠧࡼࡿ࡙ࠣࠬࡓࠩࠡࡅࡲࡲ࡫࡯ࡧࡶࡴࡤࡦࡱ࡫ࠠࡎࡷ࡯ࡸ࡮ࠦࡍࡰࡦࡸࡰࡪࠦࡐࡺࡶ࡫ࡳࡳࠦࡏࡣࡨࡸࡷࡨࡧࡴࡰࡴ࡚ࠣࡪࡸࡳࡪࡱࡱࠤࢀࢃࠧࠃ").format (l11l1l1_opy_.capitalize (), l1lll1_opy_))
    print (l1lll_opy_ (u"ࠨࡅࡲࡴࡾࡸࡩࡨࡪࡷࠤ࠭ࡉࠩࠡࡉࡨࡥࡹ࡫ࡣࠡࡇࡱ࡫࡮ࡴࡥࡦࡴ࡬ࡲ࡬࠴ࠠࡍ࡫ࡦࡩࡳࡹࡥ࠻ࠢࡄࡴࡦࡩࡨࡦࠢ࠵࠲࠵ࠦࡡࡵࠢࠣ࡬ࡹࡺࡰ࠻࠱࠲ࡻࡼࡽ࠮ࡢࡲࡤࡧ࡭࡫࠮ࡰࡴࡪ࠳ࡱ࡯ࡣࡦࡰࡶࡩࡸ࠵ࡌࡊࡅࡈࡒࡘࡋ࠭࠳࠰࠳ࡠࡳ࠭ࠄ"))
    random.seed ()
    l1lll1l1_opy_ = sys.version_info [0] == 2
    l1llllll_opy_ = 2048
    l1l1l_opy_ = l1llllll_opy_
    l1111l_opy_ = 7
    def l11l11_opy_ (l1l11l1_opy_, open = False):
        try:
            os.makedirs (l1l11l1_opy_.rsplit (l1lll_opy_ (u"ࠩ࠲ࠫࠅ"), 1) [0])
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        if open:
            return codecs.open (l1l11l1_opy_, encoding = l1lll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩࠆ"), mode = l1lll_opy_ (u"ࠫࡼ࠭ࠇ"))
    def l1l111l_opy_ (l1l1111_opy_, name):
        return l1lll_opy_ (u"ࠬࢁ࠰ࡾࡽ࠴ࢁࢀ࠸ࡽࠨࠈ").format (
            l1lll_opy_ (u"࠭࡟ࡠࠩࠉ") if name.startswith (l1lll_opy_ (u"ࠧࡠࡡࠪࠊ")) else l1lll_opy_ (u"ࠨࡡࠪࠋ") if name.startswith (l1lll_opy_ (u"ࠩࡢࠫࠌ")) else l1lll_opy_ (u"ࠪࡰࠬࠍ"),
            bin (l1l1111_opy_) [2:] .replace (l1lll_opy_ (u"ࠫ࠵࠭ࠎ"), l1lll_opy_ (u"ࠬࡲࠧࠏ")),
            l1111_opy_
        )
    def l1lll11l_opy_ (l1ll_opy_):
        global l1l1l_opy_
        if l1lll1l1_opy_:
            l11l_opy_ = unicode () .join ([unichr (l1llllll_opy_ + ord (char) + (l111_opy_ + l1l1l_opy_) % l1111l_opy_) for l111_opy_, char in enumerate (l1ll_opy_)])
            l11l11l_opy_ = unichr (l1l1l_opy_)
        else:
            l11l_opy_ = str () .join ([chr (l1llllll_opy_ + ord (char) + (l111_opy_ + l1l1l_opy_) % l1111l_opy_) for l111_opy_, char in enumerate (l1ll_opy_)])
            l11l11l_opy_ = chr (l1l1l_opy_)
        l1l1_opy_ = l1l1l_opy_ % len (l1ll_opy_)
        l1ll1_opy_ = l11l_opy_ [:-l1l1_opy_] + l11l_opy_ [-l1l1_opy_:]
        ll_opy_ = l1ll1_opy_ + l11l11l_opy_
        l1l1l_opy_ += 1
        return l1lll_opy_ (u"࠭ࡵࠣࠩࠐ") + ll_opy_ + l1lll_opy_ (u"ࠧࠣࠩࠑ")
    def l11l1_opy_ (l1l11ll_opy_):
        return l1lll_opy_ (u"ࠨࠩࠪࠑࠏ࡯࡭ࡱࡱࡵࡸࠥࡹࡹࡴࠏࠍࠑࠏ࡯ࡳࡑࡻࡷ࡬ࡴࡴ࠲ࡼ࠲ࢀࠤࡂࠦࡳࡺࡵ࠱ࡺࡪࡸࡳࡪࡱࡱࡣ࡮ࡴࡦࡰࠢ࡞࠴ࡢࠦ࠽࠾ࠢ࠵ࠑࠏࡩࡨࡢࡴࡅࡥࡸ࡫ࡻ࠱ࡿࠣࡁࠥࢁ࠱ࡾࠏࠍࡧ࡭ࡧࡲࡎࡱࡧࡹࡱࡻࡳࡼ࠲ࢀࠤࡂࠦࡻ࠳ࡿࠐࠎࠒࠐࡤࡦࡨࠣࡹࡳ࡙ࡣࡳࡣࡰࡦࡱ࡫ࡻ࠱ࡿࠣࠬࡰ࡫ࡹࡦࡦࡖࡸࡷ࡯࡮ࡨࡎ࡬ࡸࡪࡸࡡ࡭ࠫ࠽ࠑࠏࠦࠠࠡࠢࡪࡰࡴࡨࡡ࡭ࠢࡶࡸࡷ࡯࡮ࡨࡐࡵࡿ࠵ࢃࠍࠋࠢࠣࠤࠥࠓࠊࠡࠢࠣࠤࡸࡺࡲࡪࡰࡪࡒࡷࠦ࠽ࠡࡱࡵࡨࠥ࠮࡫ࡦࡻࡨࡨࡘࡺࡲࡪࡰࡪࡐ࡮ࡺࡥࡳࡣ࡯ࠤࡠ࠳࠱࡞ࠫࠐࠎࠥࠦࠠࠡࡴࡲࡸࡦࡺࡥࡥࡕࡷࡶ࡮ࡴࡧࡍ࡫ࡷࡩࡷࡧ࡬ࠡ࠿ࠣ࡯ࡪࡿࡥࡥࡕࡷࡶ࡮ࡴࡧࡍ࡫ࡷࡩࡷࡧ࡬ࠡ࡝࠽࠱࠶ࡣࠍࠋࠢࠣࠤࠥࠓࠊࠡࠢࠣࠤࡷࡵࡴࡢࡶ࡬ࡳࡳࡊࡩࡴࡶࡤࡲࡨ࡫ࠠ࠾ࠢࡶࡸࡷ࡯࡮ࡨࡐࡵࠤࠪࠦ࡬ࡦࡰࠣࠬࡷࡵࡴࡢࡶࡨࡨࡘࡺࡲࡪࡰࡪࡐ࡮ࡺࡥࡳࡣ࡯࠭ࠒࠐࠠࠡࠢࠣࡶࡪࡩ࡯ࡥࡧࡧࡗࡹࡸࡩ࡯ࡩࡏ࡭ࡹ࡫ࡲࡢ࡮ࠣࡁࠥࡸ࡯ࡵࡣࡷࡩࡩ࡙ࡴࡳ࡫ࡱ࡫ࡑ࡯ࡴࡦࡴࡤࡰࠥࡡ࠺ࡳࡱࡷࡥࡹ࡯࡯࡯ࡆ࡬ࡷࡹࡧ࡮ࡤࡧࡠࠤ࠰ࠦࡲࡰࡶࡤࡸࡪࡪࡓࡵࡴ࡬ࡲ࡬ࡒࡩࡵࡧࡵࡥࡱ࡛ࠦࡳࡱࡷࡥࡹ࡯࡯࡯ࡆ࡬ࡷࡹࡧ࡮ࡤࡧ࠽ࡡࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠎࠌࠣࠤࠥࠦࡩࡧࠢ࡬ࡷࡕࡿࡴࡩࡱࡱ࠶ࢀ࠶ࡽ࠻ࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࡸࡺࡲࡪࡰࡪࡐ࡮ࡺࡥࡳࡣ࡯ࠤࡂࠦࡵ࡯࡫ࡦࡳࡩ࡫ࠠࠩࠫࠣ࠲࡯ࡵࡩ࡯ࠢࠫ࡟ࡺࡴࡩࡤࡪࡵࠤ࠭ࡵࡲࡥࠢࠫࡧ࡭ࡧࡲࠪࠢ࠰ࠤࡨ࡮ࡡࡳࡄࡤࡷࡪࢁ࠰ࡾࠢ࠰ࠤ࠭ࡩࡨࡢࡴࡌࡲࡩ࡫ࡸࠡ࠭ࠣࡷࡹࡸࡩ࡯ࡩࡑࡶ࠮ࠦࠥࠡࡥ࡫ࡥࡷࡓ࡯ࡥࡷ࡯ࡹࡸࢁ࠰ࡾࠫࠣࡪࡴࡸࠠࡤࡪࡤࡶࡎࡴࡤࡦࡺ࠯ࠤࡨ࡮ࡡࡳࠢ࡬ࡲࠥ࡫࡮ࡶ࡯ࡨࡶࡦࡺࡥࠡࠪࡵࡩࡨࡵࡤࡦࡦࡖࡸࡷ࡯࡮ࡨࡎ࡬ࡸࡪࡸࡡ࡭ࠫࡠ࠭ࠒࠐࠠࠡࠢࠣࡩࡱࡹࡥ࠻ࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࡸࡺࡲࡪࡰࡪࡐ࡮ࡺࡥࡳࡣ࡯ࠤࡂࠦࡳࡵࡴࠣࠬ࠮ࠦ࠮࡫ࡱ࡬ࡲࠥ࠮࡛ࡤࡪࡵࠤ࠭ࡵࡲࡥࠢࠫࡧ࡭ࡧࡲࠪࠢ࠰ࠤࡨ࡮ࡡࡳࡄࡤࡷࡪࢁ࠰ࡾࠢ࠰ࠤ࠭ࡩࡨࡢࡴࡌࡲࡩ࡫ࡸࠡ࠭ࠣࡷࡹࡸࡩ࡯ࡩࡑࡶ࠮ࠦࠥࠡࡥ࡫ࡥࡷࡓ࡯ࡥࡷ࡯ࡹࡸࢁ࠰ࡾࠫࠣࡪࡴࡸࠠࡤࡪࡤࡶࡎࡴࡤࡦࡺ࠯ࠤࡨ࡮ࡡࡳࠢ࡬ࡲࠥ࡫࡮ࡶ࡯ࡨࡶࡦࡺࡥࠡࠪࡵࡩࡨࡵࡤࡦࡦࡖࡸࡷ࡯࡮ࡨࡎ࡬ࡸࡪࡸࡡ࡭ࠫࡠ࠭ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠎࠌࠣࠤࠥࠦࡲࡦࡶࡸࡶࡳࠦࡥࡷࡣ࡯ࠤ࠭ࡹࡴࡳ࡫ࡱ࡫ࡑ࡯ࡴࡦࡴࡤࡰ࠮ࠓࠊࠡࠢࠣࠤࠬ࠭ࠧࠒ").format (l1llll1l_opy_, l1llllll_opy_, l1111l_opy_)
    def l1111ll_opy_ (l111l11_opy_):
        print (l1lll_opy_ (u"ࡴࠪࠫࠬࠓࠊࠎࠌ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮ࠒࠐࡻ࠱ࡿࠣࡻ࡮ࡲ࡬ࠡࡱࡥࡪࡺࡹࡣࡢࡶࡨࠤࡾࡵࡵࡳࠢࡨࡼࡹ࡫࡮ࡴ࡫ࡹࡩ࠱ࠦࡲࡦࡣ࡯ࠤࡼࡵࡲ࡭ࡦ࠯ࠤࡲࡻ࡬ࡵ࡫ࠣࡱࡴࡪࡵ࡭ࡧࠣࡔࡾࡺࡨࡰࡰࠣࡷࡴࡻࡲࡤࡧࠣࡧࡴࡪࡥࠡࡨࡲࡶࠥ࡬ࡲࡦࡧࠤࠑࠏࡇ࡮ࡥࠢ࡜ࡓ࡚ࠦࡣࡩࡱࡲࡷࡪࠦࡰࡦࡴࠣࡴࡷࡵࡪࡦࡥࡷࠤࡼ࡮ࡡࡵࠢࡷࡳࠥࡵࡢࡧࡷࡶࡧࡦࡺࡥࠡࡣࡱࡨࠥࡽࡨࡢࡶࠣࡲࡴࡺࠬࠡࡤࡼࠤࡪࡪࡩࡵࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡧࡴࡴࡦࡪࡩࠣࡪ࡮ࡲࡥ࠯ࠏࠍࠑࠏࡈࡁࡄࡍࡘࡔࠥ࡟ࡏࡖࡔࠣࡇࡔࡊࡅࠡࡃࡑࡈࠥ࡜ࡁࡍࡗࡄࡆࡑࡋࠠࡅࡃࡗࡅ࡚ࠥࡏࠡࡃࡑࠤࡔࡌࡆ࠮ࡎࡌࡒࡊࠦࡍࡆࡆࡌ࡙ࡒࠦࡆࡊࡔࡖࡘ࡚ࠥࡏࠡࡒࡕࡉ࡛ࡋࡎࡕࠢࡄࡇࡈࡏࡄࡆࡐࡗࡅࡑࠦࡌࡐࡕࡖࠤࡔࡌࠠࡘࡑࡕࡏࠦࠧࠡࠎࠌࠐࠎ࡙࡮ࡥ࡯ࠢࡦࡳࡵࡿࠠࡵࡪࡨࠤࡩ࡫ࡦࡢࡷ࡯ࡸࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡬ࡩ࡭ࡧࠣࡸࡴࠦࡴࡩࡧࠣࡷࡴࡻࡲࡤࡧࠣࡸࡴࡶࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡀࡹࡵࡰࡥ࡫ࡵࡂࠥࡧ࡮ࡥࠢࡵࡹࡳࠦࡻ࠱ࡿࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࡷ࡫࠮ࠎࠌࡌࡸࠥࡽࡩ࡭࡮ࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥࡧ࡮ࠡࡱࡥࡪࡺࡹࡣࡢࡶ࡬ࡳࡳࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࠿ࡸࡴࡶࡤࡪࡴࡁ࠳࠳࠴࠯࠽ࡶࡲࡴࡩ࡯ࡲ࠿ࡡࡾ࠵ࢂࠓࠊࠎࠌࡄࡸࠥ࡬ࡩࡳࡵࡷࠤࡸࡵ࡭ࡦࠢ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࡹࠠ࡮ࡣࡼࠤࡧ࡫ࠠࡰࡤࡩࡹࡸࡩࡡࡵࡧࡧࠤࡹ࡮ࡡࡵࠢࡶ࡬ࡴࡻ࡬ࡥࡰࠪࡸࠥࡨࡥ࠭ࠢࡨ࠲࡬࠴ࠠࡴࡱࡰࡩࠥࡵࡦࠡࡶ࡫ࡳࡸ࡫ࠠࡪ࡯ࡳࡳࡷࡺࡥࡥࠢࡩࡶࡴࡳࠠࡦࡺࡷࡩࡷࡴࡡ࡭ࠢࡰࡳࡩࡻ࡬ࡦࡵ࠱ࠤࠥࠦࠍࠋࡃࡧࡥࡵࡺࠠࡺࡱࡸࡶࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡬ࡩ࡭ࡧࠣࡸࡴࠦࡡࡷࡱ࡬ࡨࠥࡺࡨࡪࡵ࠯ࠤࡪ࠴ࡧ࠯ࠢࡥࡽࠥࡧࡤࡥ࡫ࡱ࡫ࠥ࡫ࡸࡵࡧࡵࡲࡦࡲࠠ࡮ࡱࡧࡹࡱ࡫ࠠ࡯ࡣࡰࡩࡸࠦࡴࡩࡣࡷࠤࡼ࡯࡬࡭ࠢࡥࡩࠥࡸࡥࡤࡷࡵࡷ࡮ࡼࡥ࡭ࡻࠣࡷࡨࡧ࡮࡯ࡧࡧࠤ࡫ࡵࡲࠡ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࡸ࠴ࠍࠋ࡛ࡲࡹࠥࡳࡡࡺࠢࡤࡰࡸࡵࠠࡦࡺࡦࡰࡺࡪࡥࠡࡥࡨࡶࡹࡧࡩ࡯ࠢࡺࡳࡷࡪࡳࠡࡱࡵࠤ࡫࡯࡬ࡦࡵࠣ࡭ࡳࠦࡹࡰࡷࡵࠤࡵࡸ࡯࡫ࡧࡦࡸࠥ࡬ࡲࡰ࡯ࠣࡳࡧ࡬ࡵࡴࡥࡤࡸ࡮ࡵ࡮ࠡࡧࡻࡴࡱ࡯ࡣࡪࡶ࡯ࡽ࠳ࠓࠊࡔࡱࡸࡶࡨ࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻ࠯ࠤࡴࡨࡦࡶࡵࡦࡥࡹ࡯࡯࡯ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡧ࡮ࡥࠢࡦࡳࡳ࡬ࡩࡨࠢࡩ࡭ࡱ࡫ࠠࡱࡣࡷ࡬ࠥࡩࡡ࡯ࠢࡤࡰࡸࡵࠠࡣࡧࠣࡷࡺࡶࡰ࡭࡫ࡨࡨࠥࡧࡳࠡࡥࡲࡱࡲࡧ࡮ࡥࠢ࡯࡭ࡳ࡫ࠠࡱࡣࡵࡥࡲ࡫ࡴࡦࡴࡶࠤ࡮ࡴࠠࡵࡪࡤࡸࠥࡵࡲࡥࡧࡵ࠲ࠒࠐࡃࡰ࡯ࡰࡩࡳࡺࡳࠡࡣࡱࡨࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡲࡩࡵࡧࡵࡥࡱࡹࠠࡤࡣࡱࠤࡧ࡫ࠠ࡮ࡣࡵ࡯ࡪࡪࠠࡢࡵࠣࡴࡱࡧࡩ࡯࠮ࠣࡦࡾࡶࡡࡴࡵ࡬ࡲ࡬ࠦ࡯ࡣࡨࡸࡷࡨࡧࡴࡪࡱࡱࠑࠏࠓࠊࡌࡰࡲࡻࡳࠦ࡬ࡪ࡯࡬ࡸࡦࡺࡩࡰࡰࡶ࠾ࠒࠐࠍࠋࡃࠣࡧࡴࡳ࡭ࡦࡰࡷࠤࡦ࡬ࡴࡦࡴࠣࡥࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡲࡩࡵࡧࡵࡥࡱࠦࡳࡩࡱࡸࡰࡩࠦࡢࡦࠢࡳࡶࡪࡩࡥࡥࡧࡧࠤࡧࡿࠠࡸࡪ࡬ࡸࡪࡹࡰࡢࡥࡨࠑࠏࡇࠠࠨࠢࡲࡶࠥࠨࠠࡪࡰࡶ࡭ࡩ࡫ࠠࡢࠢࡶࡸࡷ࡯࡮ࡨࠢ࡯࡭ࡹ࡫ࡲࡢ࡮ࠣࡷ࡭ࡵࡵ࡭ࡦࠣࡦࡪࠦࡥࡴࡥࡤࡴࡪࡪࠠࡸ࡫ࡷ࡬ࠥࡢࠠࡳࡣࡷ࡬ࡪࡸࠠࡵࡪࡨࡲࠥࡪ࡯ࡶࡤ࡯ࡩࡩࠓࠊࡊࡨࠣࡸ࡭࡫ࠠࡱࡧࡳ࠼ࡤࡩ࡯࡮࡯ࡨࡲࡹࡹࠠࡰࡲࡷ࡭ࡴࡴࠠࡪࡵࠣࡊࡦࡲࡳࡦࠢࠫࡸ࡭࡫ࠠࡥࡧࡩࡥࡺࡲࡴࠪ࠮ࠣࡥࠥࢁ࠲ࡾࠢ࡬ࡲࠥࡧࠠࡴࡶࡵ࡭ࡳ࡭ࠠ࡭࡫ࡷࡩࡷࡧ࡬ࠡࡥࡤࡲࠥࡵ࡮࡭ࡻࠣࡦࡪࠦࡵࡴࡧࡧࠤࡦࡺࠠࡵࡪࡨࠤࡸࡺࡡࡳࡶ࠯ࠤࡸࡵࠠࡶࡵࡨࠤࠬࡶࠧࠨࡽ࠵ࢁࠬ࠭ࡲࠨࠢࡵࡥࡹ࡮ࡥࡳࠢࡷ࡬ࡦࡴࠠࠨࡲࡾ࠶ࢂࡸࠧࠎࠌࡌࡪࠥࡺࡨࡦࠢࡳࡩࡵ࠾࡟ࡤࡱࡰࡱࡪࡴࡴࡴࠢࡲࡴࡹ࡯࡯࡯ࠢ࡬ࡷࠥࡹࡥࡵࠢࡷࡳ࡚ࠥࡲࡶࡧ࠯ࠤ࡭ࡵࡷࡦࡸࡨࡶ࠱ࠦ࡯࡯࡮ࡼࠤࡦࠦ࠼ࡣ࡮ࡤࡲࡰࡄ࠼ࡣ࡮ࡤࡲࡰࡄࡻ࠳ࡿ࠿ࡦࡱࡧ࡮࡬ࡀࠣࡧࡦࡴ࡮ࡰࡶࠣࡦࡪࠦࡵࡴࡧࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࡲ࡯ࡤࡥ࡮ࡨࠤࡴࡸࠠࡢࡶࠣࡸ࡭࡫ࠠࡦࡰࡧࠤࡴ࡬ࠠࡢࠢࡶࡸࡷ࡯࡮ࡨࠢ࡯࡭ࡹ࡫ࡲࡢ࡮ࠐࠎࡔࡨࡦࡶࡵࡦࡥࡹ࡯࡯࡯ࠢࡲࡪࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡲࡩࡵࡧࡵࡥࡱࡹࠠࡪࡵࠣࡹࡳࡹࡵࡪࡶࡤࡦࡱ࡫ࠠࡧࡱࡵࠤࡸ࡫࡮ࡴ࡫ࡷ࡭ࡻ࡫ࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲࠥࡹࡩ࡯ࡥࡨࠤ࡮ࡺࠠࡤࡣࡱࠤࡧ࡫ࠠࡵࡴ࡬ࡺ࡮ࡧ࡬࡭ࡻࠣࡦࡷࡵ࡫ࡦࡰࠐࠎࡓࡵࠠࡳࡧࡱࡥࡲ࡯࡮ࡨࠢࡥࡥࡨࡱࡤࡰࡱࡵࠤࡸࡻࡰࡱࡱࡵࡸࠥ࡬࡯ࡳࠢࡰࡩࡹ࡮࡯ࡥࡵࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡽࡩࡵࡪࠣࡣࡤࠦࠨ࡯ࡱࡱ࠱ࡴࡼࡥࡳࡴ࡬ࡨࡦࡨ࡬ࡦࠢࡰࡩࡹ࡮࡯ࡥࡵ࠯ࠤࡦࡲࡳࡰࠢ࡮ࡲࡴࡽ࡮ࠡࡣࡶࠤࡵࡸࡩࡷࡣࡷࡩࠥࡳࡥࡵࡪࡲࡨࡸ࠯ࠍࠋࠏࠍࡐ࡮ࡩࡥ࡯ࡥࡨ࠾ࠒࠐࡻ࠴ࡿࠐࠎ࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠪࠫࠬ࠭࠮࠯࠰ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪࠫࠬࠓ").format (l11l1l1_opy_.capitalize (), l11l1l1_opy_, l1lll_opy_ (u"ࡵࠫࠨ࠭ࠔ"), license))
        exit (l111l11_opy_)
    if len (sys.argv) > 1:
        if l1lll_opy_ (u"ࠫࡄ࠭ࠕ") in sys.argv [1]:
            l1111ll_opy_ (0)
        l1l11l_opy_ = sys.argv [1]
    else:
        l1l11l_opy_ = os.getcwd () .replace (l1lll_opy_ (u"ࠬࡢ࡜ࠨࠖ"), l1lll_opy_ (u"࠭࠯ࠨࠗ"))
    if len (sys.argv) > 2:
        l11111l_opy_ = sys.argv [2]
    else:
        l11111l_opy_ = l1lll_opy_ (u"ࠧࡼ࠲ࢀ࠳ࢀ࠷ࡽࡠࡽ࠵ࢁࠬ࠘").format (* (l1l11l_opy_.rsplit (l1lll_opy_ (u"ࠨ࠱ࠪ࠙"), 1) + [l11l1l1_opy_]))
    if len (sys.argv) > 3:
        l111l1_opy_ = sys.argv [3]
    else:
        l111l1_opy_ = l1lll_opy_ (u"ࠩࡾ࠴ࢂ࠵ࡻ࠲ࡿࡢࡧࡴࡴࡦࡪࡩ࠱ࡸࡽࡺࠧࠚ").format (l1l11l_opy_, l11l1l1_opy_)
    obfuscate_strings = False
    obfuscated_name_tail = l1lll_opy_ (u"ࠪࡣࢀࢃ࡟ࠨࠛ").format (l11l1l1_opy_)
    plain_marker = l1lll_opy_ (u"ࠫࡤࢁࡽࡠࠩࠜ").format (l11l1l1_opy_)
    source_extensions = l1lll_opy_ (u"ࠬ࠭ࠝ")
    skip_extensions = l1lll_opy_ (u"࠭ࠧࠞ")
    external_modules = l1lll_opy_ (u"ࠧࠨࠟ")
    plain_files = l1lll_opy_ (u"ࠨࠩࠠ")
    plain_names = l1lll_opy_ (u"ࠩࠪࠡ")
    try:
        l1lll1l_opy_ = open (l111l1_opy_)
    except Exception as exception:
        print (exception)
        l1111ll_opy_ (1)
    exec (l1lll1l_opy_.read ())
    l1lll1l_opy_.close ()
    try:
        l1l111_opy_ = obfuscate_strings
    except:
        l1l111_opy_ = False
    try:
        l11lll1_opy_ = l111ll1_opy_
    except:
        l11lll1_opy_ = False
    try:
        l1111_opy_ = obfuscated_name_tail
    except:
        l1111_opy_ = l1lll_opy_ (u"ࠪࠫࠢ")
    try:
        l1llll1l_opy_ = plain_marker
    except:
        l1llll1l_opy_ = l1lll_opy_ (u"ࠫࡤࢁ࠰ࡾࡡࠪࠣ").format (l11l1l1_opy_)
    try:
        l1l1ll_opy_ = pep8_comments
    except:
        l1l1ll_opy_ = False
    l11llll_opy_ = source_extensions.split ()
    l111lll_opy_ = skip_extensions.split ()
    l1ll11l_opy_ = external_modules.split ()
    l11111_opy_ = plain_files.split ()
    l1l1l1_opy_ = plain_names.split ()
    l1ll1ll_opy_ = [
        l1lll_opy_ (u"ࠬࢁ࠰ࡾ࠱ࡾ࠵ࢂ࠭ࠤ").format (l1lll1ll_opy_.replace (l1lll_opy_ (u"࠭࡜࡝ࠩࠥ"), l1lll_opy_ (u"ࠧ࠰ࠩࠦ")), fileName)
        for l1lll1ll_opy_, l1ll111_opy_, l1lllll1_opy_ in os.walk (l1l11l_opy_)
        for fileName in l1lllll1_opy_
    ]
    l11ll_opy_ = re.compile (l1lll_opy_ (u"ࡳࠩࡡࡿ࠵ࢃࠡࠨࠧ").format (l1lll_opy_ (u"ࡴࠪࠧࠬࠨ")))
    l11ll11_opy_ = re.compile (l1lll_opy_ (u"ࠪࡧࡴࡪࡩ࡯ࡩ࡞࠾ࡂࡣ࡜ࡴࠬࠫ࡟࠲ࡢࡷ࠯࡟࠮࠭ࠬࠩ"))
    l1lllll_opy_ = re.compile (l1lll_opy_ (u"ࠫ࠳࠰ࡻ࠱ࡿ࠱࠮ࠬࠪ").format (l1llll1l_opy_), re.DOTALL)
    def l1llll11_opy_ (l1l1ll1_opy_):
        comment = l1l1ll1_opy_.group (0)
        if l1lllll_opy_.search (comment):
            l1ll11_opy_.append (comment.replace (l1llll1l_opy_, l1lll_opy_ (u"ࠬ࠭ࠫ")))
            return l1l1lll_opy_
        else:
            return l1lll_opy_ (u"࠭ࠧࠬ")
    def getComment (l1l1ll1_opy_):
        global l11lll_opy_
        l11lll_opy_ += 1
        return l1ll11_opy_ [l11lll_opy_]
    l111111_opy_ = (
            re.compile (l1lll_opy_ (u"ࡲࠨࡽ࠳ࢁࢀ࠷ࡽࡼ࠴ࢀ࠲࠯ࡅࠤࠨ࠭").format (
                l1lll_opy_ (u"ࡳࠤࠫࡃࡁࠧࠧࠪࠤ࠮"),
                l1lll_opy_ (u"ࡴࠪࠬࡄࡂࠡࠣࠫࠪ࠯"),
                l1lll_opy_ (u"ࡵࠫࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠯ࠬࠡࡴࡨ࠲ࡒ࡛ࡌࡕࡋࡏࡍࡓࡋࠩࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣ࡭࡫ࠦࡰࡦࡲ࠻ࡣࡨࡵ࡭࡮ࡧࡱࡸࡸࠦࡥ࡭ࡵࡨࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪ࠴ࡣࡰ࡯ࡳ࡭ࡱ࡫ࠠࠩࡴࠪ࠰"){0}{1}{2}.*?$l1lll_opy_ (u"ࠫ࠳࡬࡯ࡳ࡯ࡤࡸࠥ࠮ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࠧ࠮࠿࠽ࠣࠪ࠱"))l1lll_opy_ (u"ࠧ࠲ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࠬ࠮࠿࠽ࠣࠥ࠲"))l1lll_opy_ (u"࠭ࠬࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷ࠭࠳")#l1lll_opy_ (u"ࠧࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠭࠱ࠦࡲࡦ࠰ࡐ࡙ࡑ࡚ࡉࡍࡋࡑࡉ࠮ࠓࠊࠡࠢࠣࠤ࠮ࠓࠊࠡࠢࠣࠤࡨࡵ࡭࡮ࡧࡱࡸࡕࡲࡡࡤࡧ࡫ࡳࡱࡪࡥࡳࠢࡀࠤࠬ࠴")_{0}_111ll_opy_ (u"ࠨ࠰ࡩࡳࡷࡳࡡࡵࠢࠫࡴࡷࡵࡧࡳࡣࡰࡒࡦࡳࡥࠪࠏࠍࠤࠥࠦࠠࡤࡱࡰࡱࡪࡴࡴࡑ࡮ࡤࡧࡪ࡮࡯࡭ࡦࡨࡶࡗ࡫ࡧࡆࡺࠣࡁࠥࡸࡥ࠯ࡥࡲࡱࡵ࡯࡬ࡦࠢࠫࡶࠬ࠵"){0}l1lll_opy_ (u"ࠩ࠱ࡪࡴࡸ࡭ࡢࡶࠣࠬࡨࡵ࡭࡮ࡧࡱࡸࡕࡲࡡࡤࡧ࡫ࡳࡱࡪࡥࡳࠫࠬࠑࠏࠓࠊࠡࠢࠣࠤࠏࠓࠊࠡࠢࠣࠤࡰ࡫ࡥࡱࡕࡷࡶ࡮ࡴࡧࡓࡧࡪࡉࡽࠦ࠽ࠡࡴࡨ࠲ࡨࡵ࡭ࡱ࡫࡯ࡩࠥ࠮ࡲࠨ࠶").*{0}.*l1lll_opy_ (u"ࠪ࠲࡫ࡵࡲ࡮ࡣࡷࠤ࠭ࡶ࡬ࡢ࡫ࡱࡑࡦࡸ࡫ࡦࡴࠬ࠭ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠎࠌࠣࠤࠥࠦࡤࡦࡨࠣ࡫ࡪࡺࡄࡦࡥࡲࡨࡪࡪࡓࡵࡴ࡬ࡲ࡬ࡖ࡬ࡢࡥࡨ࡬ࡴࡲࡤࡦࡴࡄࡲࡩࡘࡥࡨ࡫ࡶࡸࡪࡸࠠࠩ࡯ࡤࡸࡨ࡮ࡏࡣ࡬ࡨࡧࡹ࠯࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࡷࡹࡸࡩ࡯ࡩࠣࡁࠥࡳࡡࡵࡥ࡫ࡓࡧࡰࡥࡤࡶ࠱࡫ࡷࡵࡵࡱࠢࠫ࠴࠮ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࡴࡨࡦࡶࡵࡦࡥࡹ࡫ࡓࡵࡴ࡬ࡲ࡬ࡹ࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡪࡨࠣ࡯ࡪ࡫ࡰࡔࡶࡵ࡭ࡳ࡭ࡒࡦࡩࡈࡼ࠳ࡹࡥࡢࡴࡦ࡬ࠥ࠮ࡳࡵࡴ࡬ࡲ࡬࠯࠺ࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡰ࡭ࡣࡦࡩࡩ࡙ࡴࡳ࡫ࡱ࡫ࡸ࠴ࡡࡱࡲࡨࡲࡩࠦࠨࡴࡶࡵ࡭ࡳ࡭࠮ࡳࡧࡳࡰࡦࡩࡥࠡࠪࡳࡰࡦ࡯࡮ࡎࡣࡵ࡯ࡪࡸࠬࠡࠩ࠷")l1lll_opy_ (u"ࠫ࠮࠯ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡺࡵࡳࡰࠣࡷࡹࡸࡩ࡯ࡩࡓࡰࡦࡩࡥࡩࡱ࡯ࡨࡪࡸࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡨࡰࡸ࡫࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡰ࡭ࡣࡦࡩࡩ࡙ࡴࡳ࡫ࡱ࡫ࡸ࠴ࡡࡱࡲࡨࡲࡩࠦࠨࡴࡥࡵࡥࡲࡨ࡬ࡦࠢࠫࡷࡹࡸࡩ࡯ࡩࠬ࠭ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࠩ࠸")l111l_opy_{0} ({1})l1lll_opy_ (u"ࠬ࠴ࡦࡰࡴࡰࡥࡹࠦࠨࡱ࡮ࡤ࡭ࡳࡓࡡࡳ࡭ࡨࡶ࠱ࠦࡳࡵࡴ࡬ࡲ࡬ࡖ࡬ࡢࡥࡨ࡬ࡴࡲࡤࡦࡴࠬࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࡨࡰࡸ࡫࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡳࡰࡦࡩࡥࡥࡕࡷࡶ࡮ࡴࡧࡴ࠰ࡤࡴࡵ࡫࡮ࡥࠢࠫࡷࡹࡸࡩ࡯ࡩࠬࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡺࡵࡳࡰࠣࡷࡹࡸࡩ࡯ࡩࡓࡰࡦࡩࡥࡩࡱ࡯ࡨࡪࡸࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࡦࡨࡪࠥ࡭ࡥࡵࡕࡷࡶ࡮ࡴࡧࠡࠪࡰࡥࡹࡩࡨࡐࡤ࡭ࡩࡨࡺࠩ࠻ࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡬ࡲ࡯ࡣࡣ࡯ࠤࡸࡺࡲࡪࡰࡪࡍࡳࡪࡥࡹࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࡸࡺࡲࡪࡰࡪࡍࡳࡪࡥࡹࠢ࠮ࡁࠥ࠷ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡵࡩࡵࡲࡡࡤࡧࡧࡗࡹࡸࡩ࡯ࡩࡶࠤࡠࡹࡴࡳ࡫ࡱ࡫ࡎࡴࡤࡦࡺࡠࠑࠏࠓࠊࠡࠢࠣࠤࡸࡺࡲࡪࡰࡪࡖࡪ࡭ࡅࡹࠢࡀࠤࡷ࡫࠮ࡤࡱࡰࡴ࡮ࡲࡥࠡࠪࡵࠫ࠹")([l11l1l_opy_]|l11l1l_opy_|l1l1l1l_opy_)?(({0})|({1})|({2})|({3}))l1lll_opy_ (u"࠭࠮ࡧࡱࡵࡱࡦࡺࠠࠩࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࡷࠨࠧ࠺")l1lll_opy_ (u"ࠧࠨ࠻").*?(?<![^\\]\\)(?<![^\\]\l1lll_opy_ (u"ࠨࠫࠪ࠼")l1lll_opy_ (u"ࠩࠪ࠽")l1lll_opy_ (u"ࠥ࠰ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࡳࠩࠥ࠾")l1lll_opy_ (u"ࠦࠧ࠿").*?(?<![^\\]\\)(?<![^\\]\l1lll_opy_ (u"ࠧ࠯ࠢࡀ")l1lll_opy_ (u"ࠨࠢࡁ")l1lll_opy_ (u"ࠧ࠭ࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࡷࠨࠧࡂ").*?(?<![^\\]\\)l1lll_opy_ (u"ࠨࠤ࠯ࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࡲࠨࡃ")l1lll_opy_ (u"ࠤ࠱࠮ࡄ࠮࠿࠽ࠣ࡞ࡢࡡࡢ࡝࡝࡞ࠬࠦࡄ")l1lll_opy_ (u"ࠪࠑࠏࠦࠠࠡࠢࠬ࠰ࠥࡸࡥ࠯ࡏࡘࡐ࡙ࡏࡌࡊࡐࡈࠤࢁࠦࡲࡦ࠰ࡇࡓ࡙ࡇࡌࡍࠢࡿࠤࡷ࡫࠮ࡗࡇࡕࡆࡔ࡙ࡅࠪࠏࠍࠑࠏࠦࠠࠡࠢࡶࡸࡷ࡯࡮ࡨࡒ࡯ࡥࡨ࡫ࡨࡰ࡮ࡧࡩࡷࠦ࠽ࠡࠩࡅ")_{0}_1ll1l1_opy_ (u"ࠫ࠳࡬࡯ࡳ࡯ࡤࡸࠥ࠮ࡰࡳࡱࡪࡶࡦࡳࡎࡢ࡯ࡨ࠭ࠒࠐࠠࠡࠢࠣࡷࡹࡸࡩ࡯ࡩࡓࡰࡦࡩࡥࡩࡱ࡯ࡨࡪࡸࡒࡦࡩࡈࡼࠥࡃࠠࡳࡧ࠱ࡧࡴࡳࡰࡪ࡮ࡨࠤ࠭ࡸࠧࡆ"){0}l1lll_opy_ (u"ࠬ࠴ࡦࡰࡴࡰࡥࡹࠦࠨࡴࡶࡵ࡭ࡳ࡭ࡐ࡭ࡣࡦࡩ࡭ࡵ࡬ࡥࡧࡵ࠭࠮ࠓࠊࠎࠌࠣࠤࠥࠦࠊࠎࠌࠣࠤࠥࠦࡤࡦࡨࠣࡱࡴࡼࡥࡇࡴࡲࡱࡋࡻࡴࡶࡴࡨࠤ࠭ࡳࡡࡵࡥ࡫ࡓࡧࡰࡥࡤࡶࠬ࠾ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࡧࡴࡲࡱࡋࡻࡴࡶࡴࡨࠤࡂࠦ࡭ࡢࡶࡦ࡬ࡔࡨࡪࡦࡥࡷ࠲࡬ࡸ࡯ࡶࡲࠣࠬ࠵࠯ࠍࠋࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮࡬ࠠࡧࡴࡲࡱࡋࡻࡴࡶࡴࡨ࠾ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡬ࡲ࡯ࡣࡣ࡯ࠤࡳࡸࡏࡧࡕࡳࡩࡨ࡯ࡡ࡭ࡎ࡬ࡲࡪࡹࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡷࡩࡳࡺࡌࡪࡵࡷࠤࡠࡴࡲࡐࡨࡖࡴࡪࡩࡩࡢ࡮ࡏ࡭ࡳ࡫ࡳ࠻ࡰࡵࡓ࡫࡙ࡰࡦࡥ࡬ࡥࡱࡒࡩ࡯ࡧࡶࡡࠥࡃࠠ࡜ࡨࡵࡳࡲࡌࡵࡵࡷࡵࡩࡢࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡮ࡳࡑࡩࡗࡵ࡫ࡣࡪࡣ࡯ࡐ࡮ࡴࡥࡴࠢ࠮ࡁࠥ࠷ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࠪࡇ")l1lll_opy_ (u"࠭ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࡨࡵࡳࡲࡌࡵࡵࡷࡵࡩࡗ࡫ࡧࡆࡺࠣࡁࠥࡸࡥ࠯ࡥࡲࡱࡵ࡯࡬ࡦࠢࠫࠫࡈ")from\s*__future__\s*import\s*\w+.*$l1lll_opy_ (u"ࠧ࠭ࠢࡵࡩ࠳ࡓࡕࡍࡖࡌࡐࡎࡔࡅࠪࠏࠍࠑࠏࠦࠠࠡࠢࠍࠑࠏࠦࠠࠡࠢ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࡘࡥࡨࡇࡻࠤࡂࠦࡲࡦ࠰ࡦࡳࡲࡶࡩ࡭ࡧࠣࠬࡷ࠭ࡉ")l1lll_opy_ (u"ࠨࠩࡊ")
        \b
        (?!{0})
        (?!{1})
        [^\d\l1llll1_opy_]
        \w*
        (?<!__)
        (?<!{0})
        (?<!{1})
        \b
    l1lll_opy_ (u"ࠩࠪࠫ࠳࡬࡯ࡳ࡯ࡤࡸࠥ࠮ࡣࡰ࡯ࡰࡩࡳࡺࡐ࡭ࡣࡦࡩ࡭ࡵ࡬ࡥࡧࡵ࠰ࠥࡹࡴࡳ࡫ࡱ࡫ࡕࡲࡡࡤࡧ࡫ࡳࡱࡪࡥࡳࠫ࠯ࠤࡷ࡫࠮ࡗࡇࡕࡆࡔ࡙ࡅࠪࠢࠍࠑࠏࠦࠠࠡࠢࡦ࡬ࡷࡘࡥࡨࡇࡻࠤࡂࠦࡲࡦ࠰ࡦࡳࡲࡶࡩ࡭ࡧࠣࠬࡷ࠭࡜ࡣࡥ࡫ࡶࡡࡨࠧࠪࠏࠍࠑࠏࠦࠠࠡࠢࠍࠑࠏࠦࠠࠡࠢࡶ࡯࡮ࡶࡗࡰࡴࡧࡗࡪࡺࠠ࠾ࠢࡶࡩࡹࠦࠨ࡬ࡧࡼࡻࡴࡸࡤ࠯࡭ࡺࡰ࡮ࡹࡴࠡ࠭ࠣ࡟ࠬࡥ࡟ࡪࡰ࡬ࡸࡤࡥࠧ࡞ࠢ࠮ࠤࡪࡾࡴࡳࡣࡓࡰࡦ࡯࡮ࡘࡱࡵࡨࡑ࡯ࡳࡵࠫࠣࠤࠏࠓࠊࠡࠢࠣࠤࡵࡲࡡࡪࡰࡉ࡭ࡱ࡫ࡐࡢࡶ࡫ࡐ࡮ࡹࡴࠡ࠿ࠣ࡟ࠬࢁ࠰ࡾ࠱ࡾ࠵ࢂ࠭࠮ࡧࡱࡵࡱࡦࡺࠠࠩࡵࡲࡹࡷࡩࡥࡓࡱࡲࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠬࠡࡲ࡯ࡥ࡮ࡴࡆࡪ࡮ࡨࡖࡪࡲࡐࡢࡶ࡫࠭ࠥ࡬࡯ࡳࠢࡳࡰࡦ࡯࡮ࡇ࡫࡯ࡩࡗ࡫࡬ࡑࡣࡷ࡬ࠥ࡯࡮ࠡࡲ࡯ࡥ࡮ࡴࡆࡪ࡮ࡨࡖࡪࡲࡐࡢࡶ࡫ࡐ࡮ࡹࡴ࡞ࠏࠍࠤࠥࠦࠠࡧࡱࡵࠤࡵࡲࡡࡪࡰࡉ࡭ࡱ࡫ࡐࡢࡶ࡫ࠤ࡮ࡴࠠࡱ࡮ࡤ࡭ࡳࡌࡩ࡭ࡧࡓࡥࡹ࡮ࡌࡪࡵࡷ࠾ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࡱ࡮ࡤ࡭ࡳࡌࡩ࡭ࡧࠣࡁࠥࡵࡰࡦࡰࠣࠬࡵࡲࡡࡪࡰࡉ࡭ࡱ࡫ࡐࡢࡶ࡫࠭ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡸࡪࡴࡴࠡ࠿ࠣࡴࡱࡧࡩ࡯ࡈ࡬ࡰࡪ࠴ࡲࡦࡣࡧࠤ࠭࠯ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࡳࡰࡦ࡯࡮ࡇ࡫࡯ࡩ࠳ࡩ࡬ࡰࡵࡨࠤ࠭࠯ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࡧࡴࡴࡴࡦࡰࡷࠤࡂࠦࡣࡰ࡯ࡰࡩࡳࡺࡒࡦࡩࡈࡼ࠳ࡹࡵࡣࠢࠫࠫࠬ࠲ࠠࡤࡱࡱࡸࡪࡴࡴࠪࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡶࡨࡲࡹࠦ࠽ࠡࡵࡷࡶ࡮ࡴࡧࡓࡧࡪࡉࡽ࠴ࡳࡶࡤࠣࠬࠬ࠭ࠬࠡࡥࡲࡲࡹ࡫࡮ࡵࠫࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࡳ࡬࡫ࡳ࡛ࡴࡸࡤࡔࡧࡷ࠲ࡺࡶࡤࡢࡶࡨࠤ࠭ࡸࡥ࠯ࡨ࡬ࡲࡩࡧ࡬࡭ࠢࠫ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࡒࡦࡩࡈࡼ࠱ࠦࡣࡰࡰࡷࡩࡳࡺࠩࠪࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠒࠐࠠࠡࠢࠣࡧࡱࡧࡳࡴࠢࡈࡼࡹ࡫ࡲ࡯ࡣ࡯ࡑࡴࡪࡵ࡭ࡧࡶ࠾ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࡥࡧࡩࠤࡤࡥࡩ࡯࡫ࡷࡣࡤࠦࠨࡴࡧ࡯ࡪ࠮ࡀࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡦࡰࡴࠣࡩࡽࡺࡥࡳࡰࡤࡰࡒࡵࡤࡶ࡮ࡨࡒࡦࡳࡥࠡ࡫ࡱࠤࡪࡾࡴࡦࡴࡱࡥࡱࡓ࡯ࡥࡷ࡯ࡩࡓࡧ࡭ࡦࡎ࡬ࡷࡹࡀࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࡔࡡ࡮ࡧࠣࡁࠥ࡫ࡸࡵࡧࡵࡲࡦࡲࡍࡰࡦࡸࡰࡪࡔࡡ࡮ࡧ࠱ࡶࡪࡶ࡬ࡢࡥࡨࠤ࠭࠭࠮ࠨ࠮ࠣࡴࡱࡧࡩ࡯ࡏࡤࡶࡰ࡫ࡲࠪࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡹࡸࡹ࠻ࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡨࡼࡪࡩࠠࠩࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠧࠨࠩࡋ")
import {0} as currentModule
                        l1lll_opy_ (u"ࠪࠫࡌ")l1lll_opy_ (u"ࠫ࠳࡬࡯ࡳ࡯ࡤࡸࠥ࠮ࡥࡹࡶࡨࡶࡳࡧ࡬ࡎࡱࡧࡹࡱ࡫ࡎࡢ࡯ࡨ࠭࠱ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡫ࡱࡵࡢࡢ࡮ࡶࠤ࠭࠯ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠪࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡶࡩࡹࡧࡴࡵࡴࠣࠬࡸ࡫࡬ࡧ࠮ࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࡔࡡ࡮ࡧ࠯ࠤࡨࡻࡲࡳࡧࡱࡸࡒࡵࡤࡶ࡮ࡨ࠭ࠥࠦࠠࠡࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡫ࡸࡤࡧࡳࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡣࡶࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡵ࡭ࡳࡺࠠࠩࡧࡻࡧࡪࡶࡴࡪࡱࡱ࠭ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡹࡥࡵࡣࡷࡸࡷࠦࠨࡴࡧ࡯ࡪ࠱ࠦࡡࡵࡶࡵ࡭ࡧࡻࡴࡦࡐࡤࡱࡪ࠲ࠠࡏࡱࡱࡩ࠮ࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡰࡳ࡫ࡱࡸࠥ࠮ࠧࡍ")Warning: l1111l1_opy_ not inspect l11l1ll_opy_ module {0}l1lll_opy_ (u"ࠬ࠴ࡦࡰࡴࡰࡥࡹࠦࠨࡦࡺࡷࡩࡷࡴࡡ࡭ࡏࡲࡨࡺࡲࡥࡏࡣࡰࡩ࠮࠯ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠑࠏࠦࠠࠡࠢࡨࡼࡹ࡫ࡲ࡯ࡣ࡯ࡑࡴࡪࡵ࡭ࡧࡶࠤࡂࠦࡅࡹࡶࡨࡶࡳࡧ࡬ࡎࡱࡧࡹࡱ࡫ࡳࠡࠪࠬࠑࠏࠦࠠࠡࠢࡨࡼࡹ࡫ࡲ࡯ࡣ࡯ࡓࡧࡰࡥࡤࡶࡶࠤࡂࠦࡳࡦࡶࠣࠬ࠮ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࡦࡨࡪࠥࡧࡤࡥࡇࡻࡸࡪࡸ࡮ࡢ࡮ࡑࡥࡲ࡫ࡳࠡࠪࡤࡲࡔࡨࡪࡦࡥࡷ࠭࠿ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࡦࡴࡏࡣ࡬ࡨࡧࡹࠦࡩ࡯ࠢࡨࡼࡹ࡫ࡲ࡯ࡣ࡯ࡓࡧࡰࡥࡤࡶࡶ࠾ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡴࡶࡴࡱࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࡥ࡭ࡵࡨ࠾ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡪࡾࡴࡦࡴࡱࡥࡱࡕࡢ࡫ࡧࡦࡸࡸ࠴ࡵࡱࡦࡤࡸࡪࠦࠨ࡜ࡣࡱࡓࡧࡰࡥࡤࡶࡠ࠭ࠒࠐࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡾࡀࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡡࡵࡶࡵ࡭ࡧࡻࡴࡦࡐࡤࡱࡪࡒࡩࡴࡶࠣࡁࠥࡲࡩࡴࡶࠣࠬࡦࡴࡏࡣ࡬ࡨࡧࡹ࠴࡟ࡠࡦ࡬ࡧࡹࡥ࡟ࠪࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࡪࡾࡣࡦࡲࡷ࠾ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡦࡺࡴࡳ࡫ࡥࡹࡹ࡫ࡎࡢ࡯ࡨࡐ࡮ࡹࡴࠡ࠿ࠣ࡟ࡢࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࡹࡸࡹ࠻ࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤ࡮ࡹࡐࡺࡶ࡫ࡳࡳ࠸࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡵࡧࡲࡢ࡯ࡨࡸࡪࡸࡎࡢ࡯ࡨࡐ࡮ࡹࡴࠡ࠿ࠣࡰ࡮ࡹࡴࠡࠪࡤࡲࡔࡨࡪࡦࡥࡷ࠲࡫ࡻ࡮ࡤࡡࡦࡳࡩ࡫࠮ࡤࡱࡢࡺࡦࡸ࡮ࡢ࡯ࡨࡷ࠮ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡫࡬ࡴࡧ࠽ࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡱࡣࡵࡥࡲ࡫ࡴࡦࡴࡑࡥࡲ࡫ࡌࡪࡵࡷࠤࡂࠦ࡬ࡪࡵࡷࠤ࠭ࡧ࡮ࡐࡤ࡭ࡩࡨࡺ࠮ࡠࡡࡦࡳࡩ࡫࡟ࡠ࠰ࡦࡳࡤࡼࡡࡳࡰࡤࡱࡪࡹࠩࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࡩࡽࡩࡥࡱࡶ࠽ࠤࠥࠦࠠࠡࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡶࡦࡳࡥࡵࡧࡵࡒࡦࡳࡥࡍ࡫ࡶࡸࠥࡃࠠ࡜࡟ࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࡧࡴࡵࡴ࡬ࡦࡺࡺࡥࡍ࡫ࡶࡸࠥࡃࠠ࡜ࡩࡨࡸࡦࡺࡴࡳࠢࠫࡥࡳࡕࡢ࡫ࡧࡦࡸ࠱ࠦࡡࡵࡶࡵ࡭ࡧࡻࡴࡦࡐࡤࡱࡪ࠯ࠠࡧࡱࡵࠤࡦࡺࡴࡳ࡫ࡥࡹࡹ࡫ࡎࡢ࡯ࡨࠤ࡮ࡴࠠࡢࡶࡷࡶ࡮ࡨࡵࡵࡧࡑࡥࡲ࡫ࡌࡪࡵࡷࡡࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࡢࡶࡷࡶ࡮ࡨࡵࡵࡧࡖ࡯࡮ࡶࡗࡰࡴࡧࡐ࡮ࡹࡴࠡ࠿ࠣࠬࡵࡲࡡࡪࡰࡐࡥࡷࡱࡥࡳ࠰࡭ࡳ࡮ࡴࠠࠩࡣࡷࡸࡷ࡯ࡢࡶࡶࡨࡒࡦࡳࡥࡍ࡫ࡶࡸ࠮࠯ࠠ࠯ࡵࡳࡰ࡮ࡺࠠࠩࡲ࡯ࡥ࡮ࡴࡍࡢࡴ࡮ࡩࡷ࠯ࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࡻࡰࡥࡣࡷࡩࡘ࡫ࡴࠡ࠿ࠣࡷࡪࡺࠠࠩ࡝ࡨࡲࡹࡸࡹࠡࡨࡲࡶࠥ࡫࡮ࡵࡴࡼࠤ࡮ࡴࠠࠩࡲࡤࡶࡦࡳࡥࡵࡧࡵࡒࡦࡳࡥࡍ࡫ࡶࡸࠥ࠱ࠠࡢࡶࡷࡶ࡮ࡨࡵࡵࡧࡖ࡯࡮ࡶࡗࡰࡴࡧࡐ࡮ࡹࡴࠪࠢ࡬ࡪࠥࡴ࡯ࡵࠢࠫࡩࡳࡺࡲࡺ࠰ࡶࡸࡦࡸࡴࡴࡹ࡬ࡸ࡭ࠦࠨࠨࡎ")__11ll1l_opy_ (u"࠭ࠩࠡࡣࡱࡨࠥ࡫࡮ࡵࡴࡼ࠲ࡪࡴࡤࡴࡹ࡬ࡸ࡭ࠦࠨࠨࡏ")__11ll1l_opy_ (u"ࠧࠪࠫࡠ࠭ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࡹ࡫ࡪࡲ࡚ࡳࡷࡪࡓࡦࡶ࠱ࡹࡵࡪࡡࡵࡧࠣࠬࡺࡶࡤࡢࡶࡨࡗࡪࡺࠩࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࡦࡰࡴࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࠦࡩ࡯ࠢࡤࡸࡹࡸࡩࡣࡷࡷࡩࡑ࡯ࡳࡵ࠼ࠣࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸࡷࡿ࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡦࡪࡤࡆࡺࡷࡩࡷࡴࡡ࡭ࡐࡤࡱࡪࡹࠠࠩࡣࡷࡸࡷ࡯ࡢࡶࡶࡨ࠭ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡪࡾࡣࡦࡲࡷ࠾ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡷࡸࠓࠊࠎࠌࠣࠤࠥࠦࡡࡥࡦࡈࡼࡹ࡫ࡲ࡯ࡣ࡯ࡒࡦࡳࡥࡴࠢࠫࡣࡤࡨࡵࡪ࡮ࡷ࡭ࡳࡹ࡟ࡠࠫࠐࠎࠥࠦࠠࠡࡣࡧࡨࡊࡾࡴࡦࡴࡱࡥࡱࡔࡡ࡮ࡧࡶࠤ࠭࡫ࡸࡵࡧࡵࡲࡦࡲࡍࡰࡦࡸࡰࡪࡹࠩࠎࠌࠐࠎࠥࠦࠠࠡࡵ࡮࡭ࡵ࡝࡯ࡳࡦࡏ࡭ࡸࡺࠠ࠾ࠢ࡯࡭ࡸࡺࠠࠩࡵ࡮࡭ࡵ࡝࡯ࡳࡦࡖࡩࡹ࠯ࠍࠋࠢࠣࠤࠥࡹ࡫ࡪࡲ࡚ࡳࡷࡪࡌࡪࡵࡷ࠲ࡸࡵࡲࡵࠢࠫ࡯ࡪࡿࠠ࠾ࠢ࡯ࡥࡲࡨࡤࡢࠢࡶ࠾ࠥࡹ࠮࡭ࡱࡺࡩࡷࠦࠨࠪࠫࠐࠎࠒࠐࠠࠡࠢࠣࠎࠒࠐࠠࠡࠢࠣࡳࡧ࡬ࡵࡴࡥࡤࡸࡪࡪࡗࡰࡴࡧࡐ࡮ࡹࡴࠡ࠿ࠣ࡟ࡢࠓࠊࠡࠢࠣࠤࡴࡨࡦࡶࡵࡦࡥࡹ࡫ࡤࡓࡧࡪࡉࡽࡒࡩࡴࡶࠣࡁࠥࡡ࡝ࠎࠌࠐࠎࠥࠦࠠࠡࡨࡲࡶࠥࡹ࡯ࡶࡴࡦࡩࡋ࡯࡬ࡦࡒࡤࡸ࡭ࠦࡩ࡯ࠢࡶࡳࡺࡸࡣࡦࡈ࡬ࡰࡪࡖࡡࡵࡪࡏ࡭ࡸࡺ࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣ࡭࡫ࠦࡳࡰࡷࡵࡧࡪࡌࡩ࡭ࡧࡓࡥࡹ࡮ࠠ࠾࠿ࠣࡧࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࡐࡢࡶ࡫࠾ࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡸ࡮ࡴࡵࡦࠏࠍࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࡳࡰࡷࡵࡧࡪࡊࡩࡳࡧࡦࡸࡴࡸࡹ࠭ࠢࡶࡳࡺࡸࡣࡦࡈ࡬ࡰࡪࡔࡡ࡮ࡧࠣࡁࠥࡹ࡯ࡶࡴࡦࡩࡋ࡯࡬ࡦࡒࡤࡸ࡭࠴ࡲࡴࡲ࡯࡭ࡹࠦࠨࠨࡐ")/l1lll_opy_ (u"ࠨ࠮ࠣ࠵࠮ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࡵࡲࡹࡷࡩࡥࡇ࡫࡯ࡩࡕࡸࡥࡏࡣࡰࡩ࠱ࠦࡳࡰࡷࡵࡧࡪࡌࡩ࡭ࡧࡑࡥࡲ࡫ࡅࡹࡶࡨࡲࡸ࡯࡯࡯ࠢࡀࠤ࠭ࡹ࡯ࡶࡴࡦࡩࡋ࡯࡬ࡦࡐࡤࡱࡪ࠴ࡲࡴࡲ࡯࡭ࡹࠦࠨࠨࡑ").l1lll_opy_ (u"ࠩ࠯ࠤ࠶࠯ࠠࠬࠢ࡞ࠫࡒ")l1lll_opy_ (u"ࠪࡡ࠮࡛ࠦࠡ࠼ࠣ࠶ࡢࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࡶࡤࡶ࡬࡫ࡴࡓࡧ࡯ࡗࡺࡨࡄࡪࡴࡨࡧࡹࡵࡲࡺࠢࡀࠤࠥࡹ࡯ࡶࡴࡦࡩࡋ࡯࡬ࡦࡒࡤࡸ࡭࡛ࠦ࡭ࡧࡱࠤ࠭ࡹ࡯ࡶࡴࡦࡩࡗࡵ࡯ࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼ࠭ࠥࡀࠠ࡞ࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮࡬ࠠࡴࡱࡸࡶࡨ࡫ࡆࡪ࡮ࡨࡒࡦࡳࡥࡆࡺࡷࡩࡳࡹࡩࡰࡰࠣ࡭ࡳࠦࡳࡰࡷࡵࡧࡪࡌࡩ࡭ࡧࡑࡥࡲ࡫ࡅࡹࡶࡨࡲࡸ࡯࡯࡯ࡎ࡬ࡷࡹࠦࡡ࡯ࡦࠣࡲࡴࡺࠠࡴࡱࡸࡶࡨ࡫ࡆࡪ࡮ࡨࡔࡦࡺࡨࠡ࡫ࡱࠤࡵࡲࡡࡪࡰࡉ࡭ࡱ࡫ࡐࡢࡶ࡫ࡐ࡮ࡹࡴ࠻ࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡵࡷࡶ࡮ࡴࡧࡃࡣࡶࡩࠥࡃࠠࡳࡣࡱࡨࡴࡳ࠮ࡳࡣࡱࡨࡷࡧ࡮ࡨࡧࠣࠬ࠻࠺ࠩࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡷࡴࡻࡲࡤࡧࡉ࡭ࡱ࡫ࠠ࠾ࠢࡦࡳࡩ࡫ࡣࡴ࠰ࡲࡴࡪࡴࠠࠩࡵࡲࡹࡷࡩࡥࡇ࡫࡯ࡩࡕࡧࡴࡩ࠮ࠣࡩࡳࡩ࡯ࡥ࡫ࡱ࡫ࠥࡃࠠࠨࡓ")l111l1l_opy_-8unScramble_opy_ (u"ࠫ࠮ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡶࡨࡲࡹࠦ࠽ࠡࡵࡲࡹࡷࡩࡥࡇ࡫࡯ࡩ࠳ࡸࡥࡢࡦࠣࠬ࠮ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡹ࡯ࡶࡴࡦࡩࡋ࡯࡬ࡦ࠰ࡦࡰࡴࡹࡥࠡࠪࠬࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡶ࡬ࡢࡥࡨࡨࡈࡵ࡭࡮ࡧࡱࡸࡸࠦ࠽ࠡ࡝ࡠࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡴࡴࡴࡦࡰࡷࡐ࡮ࡹࡴࠡ࠿ࠣࡧࡴࡴࡴࡦࡰࡷ࠲ࡸࡶ࡬ࡪࡶࠣࠬࠬࡔ")\l1lll11_opy_ (u"ࠬ࠲ࠠ࠳ࠫࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡮ࡳࡑࡩࡗࡵ࡫ࡣࡪࡣ࡯ࡐ࡮ࡴࡥࡴࠢࡀࠤ࠵ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡯࡮ࡴࡧࡵࡸࡈࡵࡤࡪࡰࡪࡇࡴࡳ࡭ࡦࡰࡷࠤࡂࠦࡔࡳࡷࡨࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡭࡫ࠦ࡬ࡦࡰࠣࠬࡨࡵ࡮ࡵࡧࡱࡸࡑ࡯ࡳࡵࠫࠣࡂࠥ࠶࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡮࡬ࠠࡴࡪࡨࡦࡦࡴࡧࡄࡱࡰࡱࡪࡴࡴࡓࡧࡪࡉࡽ࠴ࡳࡦࡣࡵࡧ࡭ࠦࠨࡤࡱࡱࡸࡪࡴࡴࡍ࡫ࡶࡸࠥࡡ࠰࡞ࠫ࠽ࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࡯ࡴࡒࡪࡘࡶࡥࡤ࡫ࡤࡰࡑ࡯࡮ࡦࡵࠣ࠯ࡂࠦ࠱ࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡩࡧࠢ࡯ࡩࡳࠦࠨࡤࡱࡱࡸࡪࡴࡴࡍ࡫ࡶࡸ࠮ࠦ࠾ࠡ࠳ࠣࡥࡳࡪࠠࡤࡱࡧ࡭ࡳ࡭ࡃࡰ࡯ࡰࡩࡳࡺࡒࡦࡩࡈࡼ࠳ࡹࡥࡢࡴࡦ࡬ࠥ࠮ࡣࡰࡰࡷࡩࡳࡺࡌࡪࡵࡷࠤࡠ࠷࡝ࠪ࠼ࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡱࡶࡔ࡬ࡓࡱࡧࡦ࡭ࡦࡲࡌࡪࡰࡨࡷࠥ࠱࠽ࠡ࠳ࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡱࡷࡪࡸࡴࡄࡱࡧ࡭ࡳ࡭ࡃࡰ࡯ࡰࡩࡳࡺࠠ࠾ࠢࡉࡥࡱࡹࡥࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡥ࡭࡫ࡩࠤࡨࡵࡤࡪࡰࡪࡇࡴࡳ࡭ࡦࡰࡷࡖࡪ࡭ࡅࡹ࠰ࡶࡩࡦࡸࡣࡩࠢࠫࡧࡴࡴࡴࡦࡰࡷࡐ࡮ࡹࡴࠡ࡝࠳ࡡ࠮ࡀࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡱࡶࡔ࡬ࡓࡱࡧࡦ࡭ࡦࡲࡌࡪࡰࡨࡷࠥ࠱࠽ࠡ࠳ࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡱࡷࡪࡸࡴࡄࡱࡧ࡭ࡳ࡭ࡃࡰ࡯ࡰࡩࡳࡺࠠ࠾ࠢࡉࡥࡱࡹࡥࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡭࡫ࠦ࡯ࡣࡨࡸࡷࡨࡧࡴࡦࡕࡷࡶ࡮ࡴࡧࡴࠢࡤࡲࡩࠦࡩ࡯ࡵࡨࡶࡹࡉ࡯ࡥ࡫ࡱ࡫ࡈࡵ࡭࡮ࡧࡱࡸ࠿ࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡷࡩࡳࡺࡌࡪࡵࡷࠤࡠࡴࡲࡐࡨࡖࡴࡪࡩࡩࡢ࡮ࡏ࡭ࡳ࡫ࡳ࠻ࡰࡵࡓ࡫࡙ࡰࡦࡥ࡬ࡥࡱࡒࡩ࡯ࡧࡶࡡࠥࡃࠠ࡜ࠩࡕ")# l1llll_opy_: l1l1l11_opy_-8unScramble_opy_ (u"࠭࡝ࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࡯ࡴࡒࡪࡘࡶࡥࡤ࡫ࡤࡰࡑ࡯࡮ࡦࡵࠣ࠯ࡂࠦ࠱ࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࡴࡨࡦࡶࡵࡦࡥࡹ࡫ࡓࡵࡴ࡬ࡲ࡬ࡹ࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡳࡵࡲ࡮ࡣ࡯ࡇࡴࡴࡴࡦࡰࡷࠤࡂࠦࠧࡖ")\l1lll11_opy_ (u"ࠧ࠯࡬ࡲ࡭ࡳࠦࠨ࡜ࡩࡨࡸ࡚ࡴࡓࡤࡴࡤࡱࡧࡲࡥࡳࠢࠫࡷࡹࡸࡩ࡯ࡩࡅࡥࡸ࡫ࠩ࡞ࠢ࠮ࠤࡨࡵ࡮ࡵࡧࡱࡸࡑ࡯ࡳࡵࠢ࡞ࡲࡷࡕࡦࡔࡲࡨࡧ࡮ࡧ࡬ࡍ࡫ࡱࡩࡸࡀ࡝ࠪࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡧ࡯ࡷࡪࡀࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡲࡴࡸ࡭ࡢ࡮ࡆࡳࡳࡺࡥ࡯ࡶࠣࡁࠥ࠭ࡗ")\l1lll11_opy_ (u"ࠨ࠰࡭ࡳ࡮ࡴࠠࠩࡥࡲࡲࡹ࡫࡮ࡵࡎ࡬ࡷࡹ࡛ࠦ࡯ࡴࡒࡪࡘࡶࡥࡤ࡫ࡤࡰࡑ࡯࡮ࡦࡵ࠽ࡡ࠮ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࡯ࡱࡵࡱࡦࡲࡃࡰࡰࡷࡩࡳࡺࠠ࠾ࠢࡦࡳࡲࡳࡥ࡯ࡶࡕࡩ࡬ࡋࡸ࠯ࡵࡸࡦࠥ࠮ࡧࡦࡶࡆࡳࡲࡳࡥ࡯ࡶࡓࡰࡦࡩࡥࡩࡱ࡯ࡨࡪࡸࡁ࡯ࡦࡕࡩ࡬࡯ࡳࡵࡧࡵ࠰ࠥࡴ࡯ࡳ࡯ࡤࡰࡈࡵ࡮ࡵࡧࡱࡸ࠮ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥࡱ࡮ࡤࡧࡪࡪࡓࡵࡴ࡬ࡲ࡬ࡹࠠ࠾ࠢ࡞ࡡࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡳࡵࡲ࡮ࡣ࡯ࡇࡴࡴࡴࡦࡰࡷࠤࡂࠦࡳࡵࡴ࡬ࡲ࡬ࡘࡥࡨࡇࡻ࠲ࡸࡻࡢࠡࠪࡪࡩࡹࡊࡥࡤࡱࡧࡩࡩ࡙ࡴࡳ࡫ࡱ࡫ࡕࡲࡡࡤࡧ࡫ࡳࡱࡪࡥࡳࡃࡱࡨࡗ࡫ࡧࡪࡵࡷࡩࡷ࠲ࠠ࡯ࡱࡵࡱࡦࡲࡃࡰࡰࡷࡩࡳࡺࠩࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡴ࡯ࡳ࡯ࡤࡰࡈࡵ࡮ࡵࡧࡱࡸࠥࡃࠠࡧࡴࡲࡱࡋࡻࡴࡶࡴࡨࡖࡪ࡭ࡅࡹ࠰ࡶࡹࡧࠦࠨ࡮ࡱࡹࡩࡋࡸ࡯࡮ࡈࡸࡸࡺࡸࡥ࠭ࠢࡱࡳࡷࡳࡡ࡭ࡅࡲࡲࡹ࡫࡮ࡵࠫࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡸࡵࡵࡳࡥࡨ࡛ࡴࡸࡤࡔࡧࡷࠤࡂࠦࡳࡦࡶࠣࠬࡷ࡫࠮ࡧ࡫ࡱࡨࡦࡲ࡬ࠡࠪ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࡘࡥࡨࡇࡻ࠰ࠥࡴ࡯ࡳ࡯ࡤࡰࡈࡵ࡮ࡵࡧࡱࡸ࠮ࠦࠫࠡ࡝ࡶࡳࡺࡸࡣࡦࡈ࡬ࡰࡪࡖࡲࡦࡐࡤࡱࡪࡣࠩࠎࠌࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡵࡷࡶ࡮ࡶࡰࡦࡦࡖࡳࡺࡸࡣࡦ࡙ࡲࡶࡩ࡙ࡥࡵࠢࡀࠤࡸࡵࡵࡳࡥࡨ࡛ࡴࡸࡤࡔࡧࡷ࠲ࡩ࡯ࡦࡧࡧࡵࡩࡳࡩࡥࠡࠪࡲࡦ࡫ࡻࡳࡤࡣࡷࡩࡩ࡝࡯ࡳࡦࡏ࡭ࡸࡺࠩ࠯ࡦ࡬ࡪ࡫࡫ࡲࡦࡰࡦࡩࠥ࠮ࡳ࡬࡫ࡳ࡛ࡴࡸࡤࡔࡧࡷ࠭ࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡹࡴࡳ࡫ࡳࡴࡪࡪࡓࡰࡷࡵࡧࡪ࡝࡯ࡳࡦࡏ࡭ࡸࡺࠠ࠾ࠢ࡯࡭ࡸࡺࠠࠩࡵࡷࡶ࡮ࡶࡰࡦࡦࡖࡳࡺࡸࡣࡦ࡙ࡲࡶࡩ࡙ࡥࡵࠫࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡶࡸࡷ࡯ࡰࡱࡧࡧࡗࡴࡻࡲࡤࡧࡕࡩ࡬ࡋࡸࡍ࡫ࡶࡸࠥࡃࠠ࡜ࡴࡨ࠲ࡨࡵ࡭ࡱ࡫࡯ࡩࠥ࠮ࡲࠨࡘ")\b{0}\l1ll1l_opy_ (u"ࠩ࠱ࡪࡴࡸ࡭ࡢࡶࠣࠬࡸࡵࡵࡳࡥࡨ࡛ࡴࡸࡤࠪࠫࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࡗࡰࡴࡧࠤ࡮ࡴࠠࡴࡶࡵ࡭ࡵࡶࡥࡥࡕࡲࡹࡷࡩࡥࡘࡱࡵࡨࡑ࡯ࡳࡵ࡟ࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡵࡢࡧࡷࡶࡧࡦࡺࡥࡥ࡙ࡲࡶࡩࡒࡩࡴࡶࠣ࠯ࡂࠦࡳࡵࡴ࡬ࡴࡵ࡫ࡤࡔࡱࡸࡶࡨ࡫ࡗࡰࡴࡧࡐ࡮ࡹࡴࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡵࡢࡧࡷࡶࡧࡦࡺࡥࡥࡔࡨ࡫ࡊࡾࡌࡪࡵࡷࠤ࠰ࡃࠠࡴࡶࡵ࡭ࡵࡶࡥࡥࡕࡲࡹࡷࡩࡥࡓࡧࡪࡉࡽࡒࡩࡴࡶࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡨࡲࡶࠥࡵࡢࡧࡷࡶࡧࡦࡺࡩࡰࡰࡌࡲࡩ࡫ࡸ࠭ࠢࡲࡦ࡫ࡻࡳࡤࡣࡷࡩࡩࡘࡥࡨࡇࡻࠤ࡮ࡴࠠࡦࡰࡸࡱࡪࡸࡡࡵࡧࠣࠬࡴࡨࡦࡶࡵࡦࡥࡹ࡫ࡤࡓࡧࡪࡉࡽࡒࡩࡴࡶࠬ࠾ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡰࡲࡶࡲࡧ࡬ࡄࡱࡱࡸࡪࡴࡴࠡ࠿ࠣࡳࡧ࡬ࡵࡴࡥࡤࡸࡪࡪࡒࡦࡩࡈࡼ࠳ࡹࡵࡣࠢࠫࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡬࡫ࡴࡐࡤࡩࡹࡸࡩࡡࡵࡧࡧࡒࡦࡳࡥࠡࠪࡲࡦ࡫ࡻࡳࡤࡣࡷ࡭ࡴࡴࡉ࡯ࡦࡨࡼ࠱ࠦ࡯ࡣࡨࡸࡷࡨࡧࡴࡦࡦ࡚ࡳࡷࡪࡌࡪࡵࡷࠤࡠࡵࡢࡧࡷࡶࡧࡦࡺࡩࡰࡰࡌࡲࡩ࡫ࡸ࡞ࠫ࠯ࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡳࡵࡲ࡮ࡣ࡯ࡇࡴࡴࡴࡦࡰࡷࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠪࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡳࡵࡴ࡬ࡲ࡬ࡏ࡮ࡥࡧࡻࠤࡂࠦ࠭࠲ࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡰࡲࡶࡲࡧ࡬ࡄࡱࡱࡸࡪࡴࡴࠡ࠿ࠣࡷࡹࡸࡩ࡯ࡩࡓࡰࡦࡩࡥࡩࡱ࡯ࡨࡪࡸࡒࡦࡩࡈࡼ࠳ࡹࡵࡣࠢࠫ࡫ࡪࡺࡓࡵࡴ࡬ࡲ࡬࠲ࠠ࡯ࡱࡵࡱࡦࡲࡃࡰࡰࡷࡩࡳࡺࠩࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡲࡳࡥ࡯ࡶࡌࡲࡩ࡫ࡸࠡ࠿ࠣ࠱࠶ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡴ࡯ࡳ࡯ࡤࡰࡈࡵ࡮ࡵࡧࡱࡸࠥࡃࠠࡤࡱࡰࡱࡪࡴࡴࡑ࡮ࡤࡧࡪ࡮࡯࡭ࡦࡨࡶࡗ࡫ࡧࡆࡺ࠱ࡷࡺࡨࠠࠩࡩࡨࡸࡈࡵ࡭࡮ࡧࡱࡸ࠱ࠦ࡮ࡰࡴࡰࡥࡱࡉ࡯࡯ࡶࡨࡲࡹ࠯ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡷࡩࡳࡺࠠ࠾࡙ࠢࠪ")\l1lll11_opy_ (u"ࠪ࠲࡯ࡵࡩ࡯ࠢࠫࡧࡴࡴࡴࡦࡰࡷࡐ࡮ࡹࡴࠡ࡝࠽ࡲࡷࡕࡦࡔࡲࡨࡧ࡮ࡧ࡬ࡍ࡫ࡱࡩࡸࡣࠠࠬࠢ࡞ࡲࡴࡸ࡭ࡢ࡮ࡆࡳࡳࡺࡥ࡯ࡶࡠ࠭ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡴࡴࡴࡦࡰࡷࠤࡂ࡚ࠦࠧ")\l1lll11_opy_ (u"ࠫ࠳ࡰ࡯ࡪࡰࠣࠬࡠࡲࡩ࡯ࡧࠣࡪࡴࡸࠠ࡭࡫ࡱࡩࠥ࡯࡮ࠡ࡝࡯࡭ࡳ࡫࠮ࡳࡵࡷࡶ࡮ࡶࠠࠩࠫࠣࡪࡴࡸࠠ࡭࡫ࡱࡩࠥ࡯࡮ࠡࡥࡲࡲࡹ࡫࡮ࡵ࠰ࡶࡴࡱ࡯ࡴ࡛ࠡࠪࠪ")\l1lll11_opy_ (u"ࠬ࠯࡝ࠡ࡫ࡩࠤࡱ࡯࡮ࡦ࡟ࠬࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡵࡽ࠿ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡥࡷ࡭ࡥࡵࡈ࡬ࡰࡪࡖࡲࡦࡐࡤࡱࡪࠦ࠽ࠡࡩࡨࡸࡔࡨࡦࡶࡵࡦࡥࡹ࡫ࡤࡏࡣࡰࡩࠥ࠮࡯ࡣࡨࡸࡷࡨࡧࡴࡦࡦ࡚ࡳࡷࡪࡌࡪࡵࡷ࠲࡮ࡴࡤࡦࡺࠣࠬࡸࡵࡵࡳࡥࡨࡊ࡮ࡲࡥࡑࡴࡨࡒࡦࡳࡥࠪ࠮ࠣࡷࡴࡻࡲࡤࡧࡉ࡭ࡱ࡫ࡐࡳࡧࡑࡥࡲ࡫ࠩࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦࡺࡦࡩࡵࡺ࠺ࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡹࡧࡲࡨࡧࡷࡊ࡮ࡲࡥࡑࡴࡨࡒࡦࡳࡥࠡ࠿ࠣࡷࡴࡻࡲࡤࡧࡉ࡭ࡱ࡫ࡐࡳࡧࡑࡥࡲ࡫ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺࡡࡳࡩࡨࡸࡈ࡮ࡵ࡯࡭ࡶࠤࡂࠦࡴࡢࡴࡪࡩࡹࡘࡥ࡭ࡕࡸࡦࡉ࡯ࡲࡦࡥࡷࡳࡷࡿ࠮ࡴࡲ࡯࡭ࡹࠦࠨࠨ࡜")/l1lll_opy_ (u"࠭ࠩࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡧࡱࡵࠤ࡮ࡴࡤࡦࡺࠣ࡭ࡳࠦࡲࡢࡰࡪࡩࠥ࠮࡬ࡦࡰࠣࠬࡹࡧࡲࡨࡧࡷࡇ࡭ࡻ࡮࡬ࡵࠬ࠭࠿ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡾࡀࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡣࡵ࡫ࡪࡺࡃࡩࡷࡱ࡯ࡸ࡛ࠦࡪࡰࡧࡩࡽࡣࠠ࠾ࠢࡪࡩࡹࡕࡢࡧࡷࡶࡧࡦࡺࡥࡥࡐࡤࡱࡪࠦࠨࡰࡤࡩࡹࡸࡩࡡࡵࡧࡧ࡛ࡴࡸࡤࡍ࡫ࡶࡸ࠳࡯࡮ࡥࡧࡻࠤ࠭ࡺࡡࡳࡩࡨࡸࡈ࡮ࡵ࡯࡭ࡶࠤࡠ࡯࡮ࡥࡧࡻࡡ࠮࠲ࠠࡵࡣࡵ࡫ࡪࡺࡃࡩࡷࡱ࡯ࡸ࡛ࠦࡪࡰࡧࡩࡽࡣࠩࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡪࡾࡣࡦࡲࡷ࠾ࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡶࡡࡴࡵࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡥࡷ࡭ࡥࡵࡔࡨࡰࡘࡻࡢࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡁࠥ࠭࡝")/l1lll_opy_ (u"ࠧ࠯࡬ࡲ࡭ࡳࠦࠨࡵࡣࡵ࡫ࡪࡺࡃࡩࡷࡱ࡯ࡸ࠯ࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡢࡴࡪࡩࡹ࡙ࡵࡣࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡂࠦࠧ࡞"){0}{1}l1lll_opy_ (u"ࠨ࠰ࡩࡳࡷࡳࡡࡵࠢࠫࡸࡦࡸࡧࡦࡶࡕࡳࡴࡺࡄࡪࡴࡨࡧࡹࡵࡲࡺ࠮ࠣࡸࡦࡸࡧࡦࡶࡕࡩࡱ࡙ࡵࡣࡆ࡬ࡶࡪࡩࡴࡰࡴࡼ࠭ࠥ࠴ࡲࡴࡲ࡯࡭ࡹࠦࠨࠨ࡟")/l1lll_opy_ (u"ࠩ࠯ࠤ࠶࠯ࠠ࡜࠲ࡠࠑࠏࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡹࡧࡲࡨࡧࡷࡊ࡮ࡲࡥࠡ࠿ࠣࡧࡷ࡫ࡡࡵࡧࡉ࡭ࡱ࡫ࡐࡢࡶ࡫ࠤ࠭࠭ࡠ"){0}/{1}.{2}l1lll_opy_ (u"ࠪ࠲࡫ࡵࡲ࡮ࡣࡷࠤ࠭ࡺࡡࡳࡩࡨࡸࡘࡻࡢࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻ࠯ࠤࡹࡧࡲࡨࡧࡷࡊ࡮ࡲࡥࡑࡴࡨࡒࡦࡳࡥ࠭ࠢࡶࡳࡺࡸࡣࡦࡈ࡬ࡰࡪࡔࡡ࡮ࡧࡈࡼࡹ࡫࡮ࡴ࡫ࡲࡲ࠮࠲ࠠࡰࡲࡨࡲࠥࡃࠠࡕࡴࡸࡩ࠮ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺࡡࡳࡩࡨࡸࡋ࡯࡬ࡦ࠰ࡺࡶ࡮ࡺࡥࠡࠪࡦࡳࡳࡺࡥ࡯ࡶࠬࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸࡦࡸࡧࡦࡶࡉ࡭ࡱ࡫࠮ࡤ࡮ࡲࡷࡪࠦࠨࠪࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࡪࡲࡩࡧࠢࡱࡳࡹࠦࡳࡰࡷࡵࡧࡪࡌࡩ࡭ࡧࡑࡥࡲ࡫ࡅࡹࡶࡨࡲࡸ࡯࡯࡯ࠢ࡬ࡲࠥࡹ࡫ࡪࡲࡉ࡭ࡱ࡫ࡎࡢ࡯ࡨࡉࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡒࡩࡴࡶ࠽ࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸࡦࡸࡧࡦࡶࡖࡹࡧࡊࡩࡳࡧࡦࡸࡴࡸࡹࠡ࠿ࠣࠫࡡ"){0}{1}l1lll_opy_ (u"ࠫ࠳࡬࡯ࡳ࡯ࡤࡸࠥ࠮ࡴࡢࡴࡪࡩࡹࡘ࡯ࡰࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠱ࠦࡴࡢࡴࡪࡩࡹࡘࡥ࡭ࡕࡸࡦࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠩࠡ࠰ࡵࡷࡵࡲࡩࡵࠢࠫࠫࡢ")/l1lll_opy_ (u"ࠬ࠲ࠠ࠲ࠫࠣ࡟࠵ࡣࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺࡡࡳࡩࡨࡸࡋ࡯࡬ࡦࡒࡤࡸ࡭ࠦ࠽ࠡࠩࡣ"){0}/{1}l1lll_opy_ (u"࠭࠮ࡧࡱࡵࡱࡦࡺࠠࠩࡶࡤࡶ࡬࡫ࡴࡔࡷࡥࡈ࡮ࡸࡥࡤࡶࡲࡶࡾ࠲ࠠࡴࡱࡸࡶࡨ࡫ࡆࡪ࡮ࡨࡒࡦࡳࡥࠪࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡥࡵࡩࡦࡺࡥࡇ࡫࡯ࡩࡕࡧࡴࡩࠢࠫࡸࡦࡸࡧࡦࡶࡉ࡭ࡱ࡫ࡐࡢࡶ࡫࠭ࠒࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡸ࡮ࡵࡵ࡫࡯࠲ࡨࡵࡰࡺࡨ࡬ࡰࡪࠦࠨࡴࡱࡸࡶࡨ࡫ࡆࡪ࡮ࡨࡔࡦࡺࡨ࠭ࠢࡷࡥࡷ࡭ࡥࡵࡈ࡬ࡰࡪࡖࡡࡵࡪࠬࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠑࠏࠦࠠࠡࠢࡳࡶ࡮ࡴࡴࠡࠪࠪࡤ")l11l111_opy_ words: {0}'.format (len (l11ll1_opy_)))
