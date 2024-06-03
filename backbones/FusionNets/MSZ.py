import torch
import torch.nn as nn
from ..SubNets.FeatureNets import BERTEncoder
from ..SubNets.AlignNets import AlignSubNet

from data.__init__ import benchmarks

__all__ = ['MSZ']

class MSZ(nn.Module):
    def __init__(self, args):
        super(MSZ, self).__init__()

        self.args = args


    def forward(self, text_feats, video_feats, audio_feats, label_ids):
        outputs = outputs

        return outputs
    
    
