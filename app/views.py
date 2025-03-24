@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        full_filename = 'images/white_bg.jpg'
        return render_template("index.html", full_filename=full_filename)  # ✅ Always return a response
    
    if request.method == "POST":
        if 'image_upload' not in request.files:
            return "No file uploaded!", 400  # ✅ Handle missing file

        image_upload = request.files['image_upload']
        if image_upload.filename == '':
            return "No selected file!", 400  # ✅ Handle empty filename
        
        imagename = image_upload.filename
        image = Image.open(image_upload)

        image_arr = np.array(image.convert('RGB'))
        gray_img_arr = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)
        image = Image.fromarray(gray_img_arr)

        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10)) + '.png'
        full_filename = 'uploads/' + name

        custom_config = r'-l eng --oem 3 --psm 6'
        text = pytesseract.image_to_string(image, config=custom_config)

        new_string = text.translate(str.maketrans("", "", "!()@—*“>+-/,'|£#%$&^_~"))
        new_string = new_string.split("\n")

        img = Image.fromarray(image_arr, 'RGB')
        img.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], name))

        return render_template('index.html', full_filename=full_filename, text=new_string)  # ✅ Always return
