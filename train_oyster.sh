python keras_retinanet/bin/train.py csv "/home/bsadrfa/behzad/projects/data_oyster/train_annotations.txt" \
  "/home/bsadrfa/behzad/projects/data_oyster/classes.txt" \
  --val-annotations "/home/bsadrfa/behzad/projects/data_oyster/test_annotations.txt" \
  --weights "snapshots/resnet50_oid_v1.0.0.h5" \
  --multi-gpu 2 \
  --freeze-backbone
# --backbone resnet50
# --epochs 50
# --lr 1e-5
