import requests, json

def getChatIds(update_url):
  response = requests.get(update_url)
  response.raise_for_status()

  # Extract the chat IDs from the updates
  updates = response.json()['result']
  chat_ids = set()
  for update in updates:
      if 'message' in update and 'chat' in update['message']:
          chat_id = update['message']['chat']['id']
          chat_type = update['message']['chat']['type']
          if chat_type == 'group' or chat_type == 'supergroup':
              chat_ids.add(chat_id)

  # Print the chat IDs
  print('Group chat IDs:')
  allChatIds = []
  for chat_id in chat_ids:
      print(chat_id)
      allChatIds.append(chat_id)
  return allChatIds


def sendPoll(poll_url,chatIds, question, options, correctOption):
  for chatId in chatIds:
    parameters = {
        "chat_id":chatId,
        "question":question,
        "options":json.dumps(options),
        "correct_option_id":correctOption,
        "type":"quiz",
    }
    resp = requests.get(poll_url, data=parameters)


