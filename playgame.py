from IPython.display import display, HTML
import uuid

game_id = "naruto_game_" + str(uuid.uuid4())[:8]

display(HTML(f"""
<style>

#game_{game_id} {{
    width: 800px;
    height: 500px;
    position: relative;
    overflow: hidden;

    border: 5px solid #111;

    background:
        radial-gradient(circle at 70% 20%, rgba(120,0,0,0.35), transparent 25%),
        linear-gradient(
            to bottom,
            #090b18 0%,
            #17152d 45%,
            #261b24 70%,
            #120d12 100%
        );

    font-family: Arial, sans-serif;
    user-select: none;
}}


/* ================================
   MOON
================================ */

.moon {{
    position: absolute;
    width: 100px;
    height: 100px;
    right: 80px;
    top: 45px;

    background: #d8d8d8;
    border-radius: 50%;

    box-shadow:
        0 0 30px rgba(255,255,255,0.25);

    z-index: 1;
}}


/* ================================
   CLOUDS
================================ */

.cloud {{
    position: absolute;
    width: 180px;
    height: 35px;

    background: rgba(30,30,45,0.85);

    border-radius: 50%;

    z-index: 2;
}}

.cloud::before {{
    content: "";
    position: absolute;

    width: 80px;
    height: 55px;

    background: rgba(30,30,45,0.85);

    border-radius: 50%;

    left: 30px;
    top: -20px;
}}

.cloud::after {{
    content: "";
    position: absolute;

    width: 70px;
    height: 50px;

    background: rgba(30,30,45,0.85);

    border-radius: 50%;

    right: 20px;
    top: -15px;
}}


/* ================================
   TREES / SHINOBI BACKGROUND
================================ */

.tree {{
    position: absolute;
    bottom: 50px;

    width: 25px;
    height: 150px;

    background: #090909;

    z-index: 3;
}}

.tree::before {{
    content: "";

    position: absolute;

    width: 100px;
    height: 100px;

    background: #080808;

    border-radius: 50%;

    left: -38px;
    top: -55px;
}}

.tree::after {{
    content: "";

    position: absolute;

    width: 90px;
    height: 90px;

    background: #080808;

    border-radius: 50%;

    left: -30px;
    top: -90px;
}}


/* ================================
   GROUND
================================ */

.ground {{
    position: absolute;

    left: 0;
    bottom: 0;

    width: 100%;
    height: 50px;

    background:
        linear-gradient(
            to bottom,
            #40302c,
            #191313
        );

    border-top: 6px solid #7b2222;

    z-index: 10;
}}


/* ================================
   PLATFORM
================================ */

.platform {{
    position: absolute;

    height: 25px;

    background: #3b2928;

    border-top: 6px solid #8b3030;

    border-radius: 5px;

    box-sizing: border-box;

    z-index: 8;
}}


/* ================================
   NARUTO PLAYER
================================ */

.player {{
    position: absolute;

    width: 45px;
    height: 65px;

    z-index: 30;
}}


/* Naruto hair */

.naruto-hair {{
    position: absolute;

    top: 0;
    left: 8px;

    width: 30px;
    height: 20px;

    background: #f5c400;

    clip-path: polygon(
        50% 0%,
        65% 20%,
        90% 5%,
        78% 40%,
        100% 30%,
        75% 60%,
        95% 70%,
        60% 65%,
        45% 100%,
        30% 65%,
        5% 75%,
        20% 45%,
        0% 40%,
        25% 20%
    );
}}


/* Naruto face */

.naruto-face {{
    position: absolute;

    top: 13px;
    left: 10px;

    width: 27px;
    height: 28px;

    background: #f2b27d;

    border-radius: 45%;
}}


/* Naruto headband */

.headband {{
    position: absolute;

    top: 14px;
    left: 7px;

    width: 33px;
    height: 8px;

    background: #222;

    z-index: 2;
}}


/* Leaf symbol */

.leaf-symbol {{
    position: absolute;

    top: 14px;
    left: 19px;

    color: #aaa;

    font-size: 8px;

    z-index: 4;
}}


/* Naruto eyes */

.naruto-eye {{
    position: absolute;

    width: 4px;
    height: 4px;

    background: #111;

    border-radius: 50%;

    top: 27px;

    z-index: 4;
}}

.naruto-eye.one {{
    left: 16px;
}}

.naruto-eye.two {{
    left: 27px;
}}


/* Naruto jacket */

.naruto-body {{
    position: absolute;

    top: 39px;
    left: 8px;

    width: 30px;
    height: 20px;

    background: #f28c28;

    border-radius: 6px;

    border-bottom: 5px solid #333;
}}


/* Legs */

.naruto-legs {{
    position: absolute;

    top: 55px;
    left: 10px;

    width: 25px;
    height: 10px;

    background: #333;

    border-radius: 5px;
}}


/* ================================
   CHAKRA ORB
================================ */

.chakra {{
    position: absolute;

    width: 24px;
    height: 24px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 30%,
            white,
            #55c7ff 20%,
            #087cff 60%,
            #003b91 100%
        );

    box-shadow:
        0 0 15px #168cff;

    z-index: 20;

    animation: chakraGlow 1s infinite alternate;
}}

@keyframes chakraGlow {{
    from {{
        transform: scale(0.9);
    }}

    to {{
        transform: scale(1.1);
    }}
}}


/* ================================
   MADARA
================================ */

.enemy {{
    position: absolute;

    width: 50px;
    height: 65px;

    z-index: 25;
}}


/* Madara hair */

.madara-hair {{
    position: absolute;

    top: 0;
    left: 5px;

    width: 40px;
    height: 35px;

    background: #080808;

    border-radius: 45% 45% 20% 20%;
}}


/* Madara face */

.madara-face {{
    position: absolute;

    top: 17px;
    left: 12px;

    width: 27px;
    height: 28px;

    background: #d69b72;

    border-radius: 45%;
}}


/* Sharingan */

.sharingan {{
    position: absolute;

    width: 9px;
    height: 9px;

    background: #b30000;

    border: 2px solid #111;

    border-radius: 50%;

    top: 25px;

    z-index: 5;
}}

.sharingan.one {{
    left: 14px;
}}

.sharingan.two {{
    right: 13px;
}}


/* Madara armor */

.madara-body {{
    position: absolute;

    top: 42px;
    left: 5px;

    width: 40px;
    height: 25px;

    background:
        linear-gradient(
            to right,
            #9e2222,
            #5c1111
        );

    border-radius: 8px;

    border: 2px solid #3b0808;
}}


/* ================================
   UI
================================ */

.ui {{
    position: absolute;

    top: 12px;
    left: 12px;
    right: 12px;

    display: flex;

    justify-content: space-between;

    z-index: 100;

    pointer-events: none;
}}

.score {{
    background: rgba(10,10,20,0.9);

    color: white;

    border: 2px solid #b52a2a;

    border-radius: 8px;

    padding: 8px 12px;

    font-size: 16px;

    font-weight: bold;

    box-shadow: 0 0 10px rgba(180,0,0,0.4);
}}


/* ================================
   TITLE
================================ */

.title {{
    position: absolute;

    top: 55px;
    left: 25px;

    color: #ffb000;

    font-size: 22px;

    font-weight: bold;

    text-shadow:
        2px 2px 5px black;

    z-index: 100;
}}


/* ================================
   MESSAGE
================================ */

.message {{
    position: absolute;

    left: 0;
    top: 0;

    width: 100%;
    height: 100%;

    background: rgba(0,0,0,0.85);

    display: none;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    color: white;

    text-align: center;

    z-index: 500;
}}

.message-title {{
    font-size: 45px;

    font-weight: bold;

    color: #ffb000;

    text-shadow:
        0 0 15px #ff5c00;
}}

.message-text {{
    font-size: 19px;

    margin-top: 12px;
}}

.restart {{
    margin-top: 25px;

    padding: 10px 25px;

    font-size: 18px;

    font-weight: bold;

    border-radius: 8px;

    border: 2px solid #a00000;

    background: #222;

    color: white;

    cursor: pointer;
}}

</style>


<div id="game_{game_id}">

    <!-- BACKGROUND -->

    <div class="moon"></div>

    <div class="cloud"
         style="left:80px; top:90px;"></div>

    <div class="cloud"
         style="left:390px; top:120px;"></div>


    <!-- TREES -->

    <div class="tree"
         style="left:40px;"></div>

    <div class="tree"
         style="left:350px;"></div>

    <div class="tree"
         style="left:700px;"></div>


    <!-- TITLE -->

    <div class="title">
        🍥 NARUTO VS MADARA ⚔️
    </div>


    <!-- PLATFORMS -->

    <div class="platform"
         style="left:120px; top:330px; width:180px;"></div>

    <div class="platform"
         style="left:400px; top:270px; width:180px;"></div>

    <div class="platform"
         style="left:620px; top:350px; width:120px;"></div>


    <!-- GROUND -->

    <div class="ground"></div>


    <!-- CHAKRA -->

    <div class="chakra"
         style="left:200px; top:290px;"></div>

    <div class="chakra"
         style="left:470px; top:230px;"></div>

    <div class="chakra"
         style="left:675px; top:310px;"></div>

    <div class="chakra"
         style="left:330px; top:400px;"></div>


    <!-- MADARA -->

    <div id="enemy_{game_id}"
         class="enemy">

        <div class="madara-hair"></div>

        <div class="madara-face"></div>

        <div class="sharingan one"></div>

        <div class="sharingan two"></div>

        <div class="madara-body"></div>

    </div>


    <!-- NARUTO -->

    <div id="player_{game_id}"
         class="player">

        <div class="naruto-hair"></div>

        <div class="naruto-face"></div>

        <div class="headband"></div>

        <div class="leaf-symbol">✦</div>

        <div class="naruto-eye one"></div>

        <div class="naruto-eye two"></div>

        <div class="naruto-body"></div>

        <div class="naruto-legs"></div>

    </div>


    <!-- UI -->

    <div class="ui">

        <div class="score"
             id="score_{game_id}">
            🔵 Chakra: 0
        </div>

        <div class="score"
             id="lives_{game_id}">
            ❤️ Lives: 3
        </div>

    </div>


    <!-- MESSAGE -->

    <div class="message"
         id="message_{game_id}">

        <div class="message-title"
             id="messageTitle_{game_id}">
            YOU WIN!
        </div>

        <div class="message-text"
             id="messageText_{game_id}">
            Naruto defeated Madara!
        </div>

        <button class="restart"
                onclick="location.reload()">
            🔄 Play Again
        </button>

    </div>

</div>


<script>

(function() {{

    const game =
        document.getElementById("game_{game_id}");

    const player =
        document.getElementById("player_{game_id}");

    const enemy =
        document.getElementById("enemy_{game_id}");

    const scoreDisplay =
        document.getElementById("score_{game_id}");

    const livesDisplay =
        document.getElementById("lives_{game_id}");

    const message =
        document.getElementById("message_{game_id}");

    const messageTitle =
        document.getElementById("messageTitle_{game_id}");

    const messageText =
        document.getElementById("messageText_{game_id}");


    /* ============================
       PLAYER
    ============================ */

    let playerX = 50;

    let playerY = 390;

    let velocityY = 0;

    const playerWidth = 45;

    const playerHeight = 65;

    const moveSpeed = 5;

    const gravity = 0.6;

    const jumpPower = -12;

    let onGround = true;


    /* ============================
       GAME
    ============================ */

    let chakra = 0;

    let lives = 3;

    let gameOver = false;


    /* ============================
       KEYBOARD
    ============================ */

    const keys = {{}};


    document.addEventListener(
        "keydown",
        function(e) {{

            const key =
                e.key.toLowerCase();

            keys[key] = true;


            if (
                (
                    key === " " ||
                    key === "arrowup" ||
                    key === "w"
                )
                &&
                onGround
                &&
                !gameOver
            ) {{

                velocityY = jumpPower;

                onGround = false;

            }}

        }}
    );


    document.addEventListener(
        "keyup",
        function(e) {{

            keys[e.key.toLowerCase()] = false;

        }}
    );


    /* ============================
       PLATFORMS
    ============================ */

    const platforms = [

        {{
            x:120,
            y:330,
            width:180,
            height:25
        }},

        {{
            x:400,
            y:270,
            width:180,
            height:25
        }},

        {{
            x:620,
            y:350,
            width:120,
            height:25
        }}

    ];


    /* ============================
       CHAKRA
    ============================ */

    const chakraElements =
        Array.from(
            game.querySelectorAll(".chakra")
        );


    const chakraData =
        chakraElements.map(function(el) {{

            return {{

                element: el,

                x: parseInt(el.style.left),

                y: parseInt(el.style.top),

                collected: false

            }};

        }});


    /* ============================
       MADARA
    ============================ */

    let enemyX = 430;

    let enemyY = 205;

    let enemyDirection = 1;

    const enemySpeed = 1.5;

    let enemyAlive = true;


    /* ============================
       COLLISION
    ============================ */

    function overlap(
        ax, ay, aw, ah,
        bx, by, bw, bh
    ) {{

        return (

            ax < bx + bw &&

            ax + aw > bx &&

            ay < by + bh &&

            ay + ah > by

        );

    }}


    /* ============================
       LOSE LIFE
    ============================ */

    function loseLife() {{

        lives--;

        livesDisplay.innerHTML =
            "❤️ Lives: " + lives;


        playerX = 50;

        playerY = 390;

        velocityY = 0;


        if (lives <= 0) {{

            gameOver = true;

            messageTitle.innerHTML =
                "💀 GAME OVER";

            messageText.innerHTML =
                "Madara defeated Naruto!";

            message.style.display =
                "flex";

        }}

    }}


    /* ============================
       COLLECT CHAKRA
    ============================ */

    function checkChakra() {{

        chakraData.forEach(
            function(item) {{

                if (item.collected) {{
                    return;
                }}


                if (
                    overlap(

                        playerX,
                        playerY,
                        playerWidth,
                        playerHeight,

                        item.x,
                        item.y,

                        24,
                        24

                    )
                ) {{

                    item.collected = true;

                    item.element.style.display =
                        "none";

                    chakra++;


                    scoreDisplay.innerHTML =
                        "🔵 Chakra: " + chakra;

                }}

            }}
        );

    }}


    /* ============================
       MADARA UPDATE
    ============================ */

    function updateEnemy() {{

        if (!enemyAlive) {{
            return;
        }}


        enemyX +=
            enemySpeed *
            enemyDirection;


        if (enemyX >= 540) {{

            enemyDirection = -1;

        }}


        if (enemyX <= 400) {{

            enemyDirection = 1;

        }}


        enemy.style.left =
            enemyX + "px";

        enemy.style.top =
            enemyY + "px";


        /* MADARA COLLISION */

        if (
            overlap(

                playerX,
                playerY,
                playerWidth,
                playerHeight,

                enemyX,
                enemyY,

                50,
                65

            )
        ) {{

            const playerBottom =
                playerY + playerHeight;


            const enemyTop =
                enemyY;


            if (
                velocityY > 0 &&
                playerBottom - enemyTop < 25
            ) {{

                /* NARUTO DEFEATS MADARA */

                enemyAlive = false;

                enemy.style.display =
                    "none";


                velocityY = -8;


                chakra += 5;


                scoreDisplay.innerHTML =
                    "🔵 Chakra: " +
                    chakra +
                    "   ⚔️ MADARA DEFEATED!";


                setTimeout(
                    function() {{

                        scoreDisplay.innerHTML =
                            "🔵 Chakra: " +
                            chakra;

                    }},
                    1200
                );

            }}

            else {{

                loseLife();

            }}

        }}

    }}


    /* ============================
       PLAYER PHYSICS
    ============================ */

    function updatePlayer() {{

        /* LEFT */

        if (
            keys["arrowleft"] ||
            keys["a"]
        ) {{

            playerX -= moveSpeed;

        }}


        /* RIGHT */

        if (
            keys["arrowright"] ||
            keys["d"]
        ) {{

            playerX += moveSpeed;

        }}


        /* SCREEN LIMITS */

        if (playerX < 0) {{

            playerX = 0;

        }}


        if (playerX > 755) {{

            playerX = 755;

        }}


        const oldBottom =
            playerY + playerHeight;


        /* GRAVITY */

        velocityY += gravity;

        playerY += velocityY;

        onGround = false;


        /* PLATFORM COLLISION */

        platforms.forEach(
            function(p) {{

                const horizontal =
                    playerX + playerWidth > p.x &&
                    playerX < p.x + p.width;


                const landing =
                    oldBottom <= p.y &&
                    playerY + playerHeight >= p.y &&
                    velocityY >= 0;


                if (
                    horizontal &&
                    landing
                ) {{

                    playerY =
                        p.y - playerHeight;

                    velocityY = 0;

                    onGround = true;

                }}

            }}
        );


        /* GROUND */

        if (playerY >= 390) {{

            playerY = 390;

            velocityY = 0;

            onGround = true;

        }}


        /* UPDATE POSITION */

        player.style.left =
            playerX + "px";

        player.style.top =
            playerY + "px";

    }}


    /* ============================
       FINISH
    ============================ */

    function checkFinish() {{

        if (
            playerX >= 720 &&
            !enemyAlive
        ) {{

            gameOver = true;


            messageTitle.innerHTML =
                "🏆 NARUTO WINS!";


            messageText.innerHTML =
                "Madara Uchiha has been defeated! " +
                "Chakra collected: " +
                chakra;


            message.style.display =
                "flex";

        }}

    }}


    /* ============================
       GAME LOOP
    ============================ */

    function gameLoop() {{

        if (!gameOver) {{

            updatePlayer();

            updateEnemy();

            checkChakra();

            checkFinish();

        }}


        requestAnimationFrame(
            gameLoop
        );

    }}


    /* START */

    gameLoop();

    console.log(
        "🍥 Naruto vs Madara Game Started!"
    );

}})();

</script>
"""))


print("🍥 NARUTO VS MADARA GAME READY!")
print()
print("⬅️ A / Left Arrow  = Move Left")
print("➡️ D / Right Arrow = Move Right")
print("⬆️ W / Up Arrow    = Jump")
print("␣ Space            = Jump")
print()
print("🔵 Collect Chakra")
print("⚔️ Jump on Madara")
print("❤️ Avoid Madara attacks")
print("🏆 Defeat Madara and reach the finish!")
