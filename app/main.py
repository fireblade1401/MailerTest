from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
import smtplib
import logging

from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates

from .models import Email
from .services import send_email

templates = Jinja2Templates(directory="templates")

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

app = FastAPI()


@app.exception_handler(ValidationError)
def validation_exception_handler(request, exc):
    logger.error(f"Ошибка валидации: {exc}")
    return JSONResponse(status_code=400, content={"error": "Ошибка валидации", "detail": exc.errors()})


@app.exception_handler(smtplib.SMTPException)
def smtp_exception_handler(request, exc):
    logger.error(f"Ошибка SMTP: {exc}")
    return JSONResponse(status_code=500, content={"error": "Ошибка при отправке письма"})


@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    logger.error(f"HTTP ошибка: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


@app.exception_handler(Exception)
def general_exception_handler(request, exc):
    logger.error(f"Неожиданная ошибка: {exc}")
    return JSONResponse(status_code=500, content={"error": "Неожиданная ошибка"})


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/send_email")
def send_email_endpoint(email: Email):
    try:
        send_email(email)
        logger.info("Письмо успешно отправлено!")
        return {"status": "success"}
    except smtplib.SMTPException as e:
        logger.error(f"Ошибка при отправке письма: {e}")
        raise HTTPException(status_code=500, detail="Ошибка при отправке письма")
