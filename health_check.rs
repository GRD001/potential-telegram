use std::time::Duration;
use reqwest::blocking::Client;

fn main() {
    // Получение аргументов командной строки
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 3 {
        eprintln!("Usage: healthcheck <URL> <interval>");
        return;
    }

    // Парсинг URL
    let url = match reqwest::Url::parse(&args[1]) {
        Ok(url) => url,
        Err(_) => {
            eprintln!("URL parsing error");
            return;
        }
    };

    // Парсинг интервала
    let interval = match args[2].parse::<u64>() {
        Ok(interval) => interval,
        Err(_) => {
            eprintln!("Invalid interval");
            return;
        }
    };

    // Создание клиента
    let client = Client::new();

    loop {
        // Отправка GET-запроса
        let response = match client.get(url.clone()).send() {
            Ok(response) => response,
            Err(_) => {
                eprintln!("Failed to send request");
                continue;
            }
        };

        // Проверка HTTP-статуса
        if response.status().is_success() {
            println!("OK(200)");
        } else {
            println!("ERR({})", response.status());
        }

        // Задержка перед следующей итерацией
        std::thread::sleep(Duration::from_secs(interval));
    }
}
