# python 001_make_dump.py
# python 002_download_images.py
THUMB_DIR=$1

# python 003_get_captures.py
# python 004_get_metadata.py
# python 005_get_color_data.py
# python 006_get_colors.py

# python 007_stitch_images.py ../data/ $THUMB_DIR/ ../../docs/pd-visualization/img/ 100 10 10 default 100 10 3 30000
python 007_stitch_images.py ../data/ $THUMB_DIR/ ../../docs/pd-visualization/img/ 100 10 10 colors 100 10 3 30000
python 007_stitch_images.py ../data/ $THUMB_DIR/ ../../docs/pd-visualization/img/ 100 10 10 基本区分 100 10 3 30000
python 007_stitch_images.py ../data/ $THUMB_DIR/ ../../docs/pd-visualization/img/ 100 10 10 収録DB 100 10 3 30000
python 007_stitch_images.py ../data/ $THUMB_DIR/ ../../docs/pd-visualization/img/ 100 10 10 所蔵機関 100 10 3 30000
python 007_stitch_images.py ../data/ $THUMB_DIR/ ../../docs/pd-visualization/img/ 100 10 10 機械タグ 100 10 3 30000

python 008_generate_metadata.py
python 009_generate_labels.py ../data/ ../../docs/pd-visualization/js/labels.json 100 10 100 10 3 #####
python 010_generate_coordinates.py ../data/ ../../docs/pd-visualization/js/coords.json 100 10 10 100 10 3 #####
