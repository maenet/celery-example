from celery import Celery, chain, group
import time


app = Celery("tasks")
app.config_from_object("celeryconfig")


@app.task(bind=True)
def example_task(self):
    print("---------------------------------------------------------------------------")
    print("id: {}".format(self.request.id))
    print("root_id: {}".format(self.request.root_id))
    print("parent_id: {}".format(self.request.parent_id))
    time.sleep(1)

    return None


def on_success(result):
    print("ok")


def on_failure(result):
    print("ng")


c = chain(
    example_task.si(), example_task.si(), group(example_task.si(), example_task.si())
)
result = c.apply_async()

parent = result
while parent.parent is not None:
    parent = parent.parent

print(parent.id)  # == root_id

# result.then(on_success, on_failure)
