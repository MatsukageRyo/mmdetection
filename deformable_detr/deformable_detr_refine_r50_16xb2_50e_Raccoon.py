_base_ = '../configs/deformable_detr/deformable-detr-refine_r50_16xb2-50e_coco.py'

data_root = "racoon_dataset"
classes = ["raccoons", "raccoon"]
train_dataloader = dict(
    dataset=dict(
        metainfo=dict(classes=classes),
        data_root=data_root,
        ann_file='train/_annotations.coco.json',
        data_prefix=dict(img='train/')
        )
    )

val_dataloader = dict(
    dataset=dict(
        test_mode=True,
        metainfo=dict(classes=classes),
        data_root=data_root,
        ann_file='valid/_annotations.coco.json',
        data_prefix=dict(img='valid/')
        )
    )

test_dataloader = dict(
    dataset=dict(
        test_mode=True,
        metainfo=dict(classes=classes),
        data_root=data_root,
        ann_file='test/_annotations.coco.json',
        data_prefix=dict(img='test/')
        )
    )

val_evaluator = dict(
    ann_file= data_root + '/valid/_annotations.coco.json',
)
test_evaluator = dict(
    ann_file = data_root + "/valid/_annotations.coco.json"
)

model = dict(
    bbox_head=dict(
        num_classes=2))

load_from = "deformable_detr/checkpoints/deformable-detr-refine_r50_16xb2-50e_coco_20221022_225303-844e0f93.pth"
