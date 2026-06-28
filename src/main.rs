use axum::{
    extract::State,
    http::StatusCode,
    response::{Html, IntoResponse, Json},
    routing::{get, post},
    Router,
};
use serde::{Deserialize, Serialize};
use std::sync::Arc;
use tower_http::services::ServeDir;

// 测试账号
const TEST_USER: &str = "liuchuan";
const TEST_PASS: &str = "lc02514";

#[derive(Deserialize)]
struct LoginRequest {
    username: String,
    password: String,
}

#[derive(Serialize)]
struct LoginResponse {
    success: bool,
    message: String,
    token: Option<String>,
}

async fn login_handler(Json(req): Json<LoginRequest>) -> impl IntoResponse {
    if req.username == TEST_USER && req.password == TEST_PASS {
        Json(LoginResponse {
            success: true,
            message: "登录成功！欢迎回来，liuchuan。".to_string(),
            token: Some("test-token-liuchuan-2026".to_string()),
        })
    } else {
        Json(LoginResponse {
            success: false,
            message: "用户名或密码错误".to_string(),
            token: None,
        })
    }
}

async fn index_handler() -> impl IntoResponse {
    Html(include_str!("../static/index.html"))
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(index_handler))
        .route("/api/login", post(login_handler))
        .nest_service("/static", ServeDir::new("static"));

    let addr = "0.0.0.0:3000";
    println!("🚀 登录页面启动在 http://127.0.0.1:3000");
    println!("  测试账号: liuchuan / lc02514");

    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
