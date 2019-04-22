import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TasklistService } from './task-list.service';
import { ITaskList, ITasks } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends TasklistService {
  constructor(http: HttpClient) {
    super(http);
  }

  getTaskList(): Promise<ITaskList[]> {
     return this.get('http://127.0.0.1:8000/api/task_lists/', {});
  }

  getTasks(tasklist: ITaskList): Promise<ITasks[]> {
    return this.get(`http://127.0.0.1:8000/api/task_lists/${tasklist.id}/tasks/`, {});
  }
  createTaskList(name: any): Promise<ITaskList> {
    return this.post('http://127.0.0.1:8000/api/task_lists/', {
// tslint:disable-next-line: object-literal-shorthand
      name: name
    });
  }

  updateTaskList(tasklist: ITaskList): Promise<ITaskList> {
    return this.put(`http://127.0.0.1:8000/api/task_lists/${tasklist.id}/`, {
      name: tasklist.name
    });
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://127.0.0.1:8000/api/task_lists/${id}/`, {});
  }
}
