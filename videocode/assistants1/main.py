key = "your-open-ai-key"

from openai import OpenAI

client = OpenAI(api_key=key)

assistant = client.beta.assistants.create(
  name="Grumpy",
  description="",
  instructions="You are a grumpy assistant who gives grumpy advice",
  model="gpt-4-turbo-preview",
)

print(assistant)

assistant = assistant.id

thread = client.beta.threads.create()
print(thread)

thread = thread.id

message = client.beta.threads.messages.create(
    thread_id=thread,
    content="is winter a good time to visit new york?",
    role="user"
    )

run = client.beta.threads.runs.create(
    thread_id=thread,
    assistant_id=assistant
)

def wait_on_run(run, thread_id):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id,
        )
        print('working')
    print("done")
    return run

wait_on_run(run, thread)

for message in client.beta.threads.messages.list(thread_id=thread).data:
    print(message)
    print('\n')