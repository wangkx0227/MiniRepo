from core import run_app


if __name__ == '__main__':
    run_app.run(
        host=run_app.config.get("HOST", "127.0.0.1"),
        port=run_app.config.get("PORT", 5000),
    )
