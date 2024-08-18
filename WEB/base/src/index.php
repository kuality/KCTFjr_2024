<html>
    <head>
        <link rel="stylesheet" href="./assets/css/main.css">
        <link rel="stylesheet" href="./assets/css/font.css">
    </head>
    <body>
        <div class="center">
            <form method="POST" action="./upload.php" enctype="multipart/form-data">
                <div class="file-upload">
                    <h1 style="padding: 0px; margin: 0px;">Drage & Drop</h1>
                    <input type="file" name="fileupload">
                </div>
                <input type="submit" value="submit" class="submit">
            </form>
        </div>
        <script>

            const fileupload = document.getElementsByClassName("file-upload")[0];
            const file = document.querySelector("input[type=file]");

            fileupload.addEventListener('click',() => {
                file.click();
            });

            fileupload.addEventListener('dragover', (e) => { e.preventDefault(); });
            fileupload.addEventListener('dragleave', (e) => {
                fileupload.style.backgroundColor = '#69CFFF';
            });
            fileupload.addEventListener('drop', (e) => {

                e.preventDefault();
                data = e.dataTransfer.files;
                name = data[0].name;

                file.files = data;

                document.querySelector(".file-upload>h1").innerText = name;

            });

            file.addEventListener('change', (e) => {
                data = e.target.files[0];
                name = data.name;
                
                document.querySelector(".file-upload>h1").innerText = name;
                
            });

        </script>

    </body>
</html>
