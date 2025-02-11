addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

/**
 * Respond to the request
 * @param {Request} request
 */
async function handleRequest(request) {
  try {
    // 获取环境变量，使用 "TOKEN" 格式
    const TG_BOT_TOKEN = TOKEN;
    const USER_ID = USER;

    // 检查环境变量是否存在
    if (!TG_BOT_TOKEN || !USER_ID) {
      console.error("Missing TG_BOT_TOKEN or USER_ID environment variables!");
      return new Response("Error: Missing TG_BOT_TOKEN or USER_ID environment variables.", { status: 500 });
    }

    console.log("TG_BOT_TOKEN:", TG_BOT_TOKEN); // 确认 Token 已加载
    console.log("USER_ID:", USER_ID); // 确认 User ID 已加载

    // 记录所有请求头
    console.log("Request headers:", JSON.stringify(Object.fromEntries(request.headers.entries())));

    // 解析请求，假设请求体是 JSON 格式，包含命令
    const requestBodyText = await request.text(); // 获取请求体文本
    console.log("Request body:", requestBodyText); // 打印请求体

    let requestBody;
    try {
      requestBody = JSON.parse(requestBodyText); // 手动解析 JSON
    } catch (jsonError) {
      console.error("JSON parsing error:", jsonError);
      return new Response(`Error: Invalid JSON format. ${jsonError.message}.  Raw body: ${requestBodyText}`, { status: 400 });
    }

    const command = requestBody.command;

    if (!command) {
      return new Response("Error: Missing 'command' in request body.", { status: 400 });
    }

    // 解析命令和参数
    const [commandName, ...commandArgs] = command.split(" ");
    const args = commandArgs.join(" ");

    let responseText = "";

    // 命令处理
    switch (commandName.toLowerCase()) {
      case "start":
        // 模拟用户数据存储 (实际应用中需要使用 KV 存储或其他数据库)
        let userRegistered = false; // 假设用户未注册

        if (userRegistered) {
          responseText = "Welcome! You can use the following commands:\n" +
            "/email - Bind your notification email.\n" +
            "/about - Get author information.\n" +
            "/goods - Get author's recommended information.";
        } else {
          responseText = "Welcome! It seems you are not registered yet. Please use the command `my <account> <password>` to register.";
        }
        break;

      case "email":
        // 处理绑定邮箱的逻辑 (实际应用中需要保存邮箱地址到 KV 存储或其他数据库)
        if (args) {
          responseText = `Successfully bound email: ${args}`;
          // TODO: 实际绑定邮箱逻辑，例如保存到 KV 存储
        } else {
          responseText = "Please provide an email address. Usage: /email <email_address>";
        }
        break;

      case "about":
        responseText = "This bot was created by [Your Name/Handle]. Contact: [Your Email/Contact Info]";
        break;

      case "goods":
        responseText = "Here are some recommended items:\n" +
          "- Item 1: [Description] - [Link]\n" +
          "- Item 2: [Description] - [Link]\n" +
          "- Item 3: [Description] - [Link]";
        break;

      case "my":
        // 模拟注册逻辑
        if (commandArgs.length === 2) {
            const account = commandArgs[0];
            const password = commandArgs[1];
            // TODO: 实际注册逻辑，例如验证账号密码，保存用户信息
            responseText = `Successfully registered account: ${account}.  **Important: This is a simulated registration.  Do not use real credentials.**`;
        } else {
            responseText = "Usage: /my <account> <password>";
        }
        break;

      default:
        responseText = "Unknown command. Please use /start for help.";
        break;
    }

    // 构建 Telegram API 请求 URL
    const apiUrl = `https://api.telegram.org/bot${TG_BOT_TOKEN}/sendMessage`;
    console.log("Telegram API URL:", apiUrl); // 确认 API URL 正确

    // 构建请求体，发送消息给指定用户
    const payload = {
      chat_id: USER_ID,
      text: responseText,
    };
    console.log("Telegram API Payload:", JSON.stringify(payload)); // 确认 Payload 正确

    // 发送请求到 Telegram API
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload),
    });

    // 处理 Telegram API 响应
    if (response.ok) {
      const responseData = await response.json();
      console.log("Telegram API Response:", JSON.stringify(responseData)); // 记录 Telegram API 响应
      return new Response(JSON.stringify({ message: "Command sent successfully!", telegramResponse: responseData }), {
        headers: {
          'Content-Type': 'application/json'
        }
      });
    } else {
      console.error("Telegram API error:", response.status, response.statusText, await response.text()); // 打印详细错误信息
      return new Response(`Error: Telegram API request failed. Status: ${response.status} ${response.statusText}`, {
        status: response.status
      });
    }

  } catch (error) {
    console.error("Error processing request:", error); // 打印详细错误信息
    return new Response(`Error: ${error.message}`, {
      status: 400
    });
  }
}
