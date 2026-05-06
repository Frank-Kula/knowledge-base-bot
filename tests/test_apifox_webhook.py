import httpx
import asyncio
import json

async def test_webhook():
    print("[Test] 准备发送模拟测试请求到本地 FastAPI 服务器...")
    url = "http://127.0.0.1:8000/webhook/apifox_wecom"
    
    # 模拟一份扣子/Apifox 协议发来的真实消息 JSON
    payload = {
      "type": "chat.message",
      "contentType": 1,
      "content": "接口测试失败，报500错误该怎么排查？",
      "chatUser": "test_user_001",
      "senderName": "测试体验员",
      "isGroupChat": 0,
      "robotKey": "test_robot_888",
      "messageId": "msg_20260311",
      "sendTime": "2026-03-11 15:00:00"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, timeout=5.0)
            
        print(f"[*] 请求发送成功！服务器状态码: {response.status_code}")
        print(f"[*] 服务器返回内容: {response.text}")
        print("\n[Tip] 现在请去查看您运行的 main.py 终端日志，看看是否成功触发了意图分析、收集信息并尝试回复消息。")
        print("[!] （因为目前环境变量的 accessKey 我们是乱填的，所以预期终端会在最后一步打印：'获取企微 Access Token 失败'。这恰恰证明整个处理链路是通的，只是卡在最后真实的发送握手上！）")
        
    except Exception as e:
        print(f"[!] 呀，发送失败了，请先确保 `python src/bots/main.py` 已经运行起来了！\n错误详情: {e}")

if __name__ == "__main__":
    asyncio.run(test_webhook())
