<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Water Logging Sign Up</title>
    <style>
        body {
            /* margin: 0; */
            /* padding: 0; */
            font-family: Arial, sans-serif; 
            background-size: cover;
            /* background-position: center; */
            background-color: black;
            /* height: 100vh; */
            display: flex;
            /* justify-content: center; */
         /* align-items: center; */
        }
        
        .container {
            width: 70%; 
            max-width: 300px; 
            background-color: dark gray;
            padding: 20px; 
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            text-align: center;
        }
        
        .content {
            display: flex;
            align-items: right;
        }
        
        .image {
            width: 50vw; /* Set width to 50% of viewport width */
            padding: 20px;
            box-sizing: border-box;
        }
        
        .image img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }
        
        h2 {
            margin-bottom: 10px;
            color: aliceblue;
        }
        
        input[type="text"], input[type="email"], input[type="password"] {
            width: 100%;
            padding: 18px;
            margin-bottom: 20px;
            border-radius: 5px;
            box-sizing: border-box;
            background-color: dark grey; 
            border: 1px solid #333; 
            color: white; 
            transition: background-color 0.3s;
        }

        input[type="text"]:focus, input[type="email"]:focus, input[type="password"]:focus {
            border-color: #4CAF50; 
            outline: none; 
            background-color: grey;
        }
        
        input[type="submit"] {
            background-color: #333;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        
        input[type="submit"]:hover {
            background-color: #555555;
        }

        .content {
            align-items: right;  
             padding-left: 70px;
            margin-left: 20px; 
        }

        .container > div {
            display: inline-block;
            background-attachment: fixed;
            width: 180%; 
            height: 100%;/* Adjusted to approximately 33.33% to accommodate three images in a row */
            margin: 20px;
            box-sizing: border-box; /* Include padding and border in the width */
        }
        .image {
            width: 50vw; /* Set width to 50% of viewport width */
            padding: 0px;
            box-sizing: border-box;
            padding-left:0px;
            height: max-content;
            
        }
    </style>
</head>
<body>

        <div class="image">
            <img src="globee.gif" alt="globe" width="800">
        </div>
        <div class="container">

        <div class="content">
            <br><br>
            <h2>Sign Up</h2><br><br>
            <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
                <input type="text" name="fullname" placeholder="Full Name" required><br>
                <input type="email" name="email" placeholder="Email" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                <br><input type="submit" value="Sign Up">
            </form>
            
        </div>
    </div>
</body>
</html>