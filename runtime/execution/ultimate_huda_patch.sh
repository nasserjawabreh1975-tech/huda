#!/bin/bash

clear

echo "======================================="
echo "      HUDA ULTIMATE PATCH ACTIVE"
echo "======================================="

BASE="$HOME/HUDA_CORE"
UI="$BASE/hudaui"

mkdir -p \
"$BASE/runtime" \
"$BASE/memory" \
"$BASE/agents" \
"$BASE/logs" \
"$BASE/uploads" \
"$BASE/api"

cd "$UI"

echo
echo "[1] CLEANING"

pkill -f vite
pkill -f node

sleep 2

echo
echo "[2] INSTALL CORE"

npm install

npm install react-router-dom
npm install axios
npm install lucide-react

echo
echo "[3] WRITING ROUTER"

mkdir -p src/pages
mkdir -p src/components

cat > src/main.jsx << 'MAIN'
import React from "react"
import ReactDOM from "react-dom/client"
import {
BrowserRouter,
Routes,
Route
} from "react-router-dom"

import "./index.css"

import Home from "./pages/Home"
import Chat from "./pages/Chat"
import Runtime from "./pages/Runtime"
import Agents from "./pages/Agents"
import Memory from "./pages/Memory"
import Logs from "./pages/Logs"
import Uploads from "./pages/Uploads"
import Engineering from "./pages/Engineering"

function App() {
return (
<BrowserRouter>
<Routes>
<Route path="/" element={<Home />} />
<Route path="/chat" element={<Chat />} />
<Route path="/runtime" element={<Runtime />} />
<Route path="/agents" element={<Agents />} />
<Route path="/memory" element={<Memory />} />
<Route path="/logs" element={<Logs />} />
<Route path="/uploads" element={<Uploads />} />
<Route path="/engineering" element={<Engineering />} />
</Routes>
</BrowserRouter>
)
}

ReactDOM.createRoot(document.getElementById("root")).render(
<App />
)
MAIN

echo
echo "[4] WRITING STYLE"

cat > src/index.css << 'CSS'
body{
margin:0;
background:#050505;
color:#00ff66;
font-family:monospace;
}

.page{
padding:30px;
}

.title{
font-size:32px;
margin-bottom:20px;
}

.card{
border:1px solid #00ff66;
padding:20px;
margin-bottom:20px;
border-radius:10px;
background:#0b0b0b;
}

.input{
width:100%;
padding:15px;
background:black;
border:1px solid #00ff66;
color:#00ff66;
margin-top:10px;
}

.button{
padding:12px 20px;
background:#00ff66;
border:none;
color:black;
font-weight:bold;
cursor:pointer;
margin-top:10px;
}
CSS

echo
echo "[5] WRITING PAGES"

for PAGE in Home Chat Runtime Agents Memory Logs Uploads Engineering
do

cat > src/pages/$PAGE.jsx << EOF2
export default function $PAGE(){

return (
<div className="page">

<div className="title">
HUDA $PAGE
</div>

<div className="card">
SYSTEM ONLINE
</div>

<div className="card">
COGNITION ACTIVE
</div>

<input
className="input"
placeholder="HUDA INPUT..."
/>

<button className="button">
EXECUTE
</button>

</div>
)
}
EOF2

done

echo
echo "[6] WRITING API"

cat > "$BASE/api/server.py" << 'PY'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_methods=["*"],
allow_headers=["*"]
)

@app.get("/")
def home():
    return {
        "status":"online",
        "system":"HUDA"
    }

@app.get("/runtime")
def runtime():
    return {
        "runtime":"active"
    }

@app.get("/memory")
def memory():
    return {
        "memory":"stable"
    }

@app.get("/agents")
def agents():
    return {
        "agents":"online"
    }

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
PY

echo
echo "[7] STARTING API"

nohup python3 "$BASE/api/server.py" \
>/tmp/huda_api.log 2>&1 &

echo
echo "[8] STARTING UI"

nohup npm run dev -- \
--host 0.0.0.0 \
--port 3300 \
>/tmp/huda_ui.log 2>&1 &

sleep 5

echo
echo "======================================="
echo "         HUDA FULLY ONLINE"
echo "======================================="
echo
echo "UI:"
echo "http://localhost:3300"
echo
echo "API:"
echo "http://localhost:8000"
echo
echo "PAGES:"
echo "/"
echo "/chat"
echo "/runtime"
echo "/agents"
echo "/memory"
echo "/logs"
echo "/uploads"
echo "/engineering"
echo
