import unittest
import numpy as np
from multimodal_self_regulation_lab.core import split_indices, fit_auc
from multimodal_self_regulation_lab.synthetic import make_multimodal

class HoldoutTests(unittest.TestCase):
    def test_shared_split_is_disjoint_and_complete(self):
        data=make_multimodal(150,4)
        train,test=split_indices(data.target.to_numpy())
        self.assertFalse(set(train)&set(test))
        self.assertEqual(len(train)+len(test),150)
        self.assertEqual(len(test),45)

    def test_overlap_is_rejected(self):
        with self.assertRaises(ValueError):
            fit_auc(np.array([[0],[1],[2],[3]]), np.array([0,1,0,1]),[0,1,2],[2,3])
