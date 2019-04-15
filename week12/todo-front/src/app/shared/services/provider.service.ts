import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TasklistService } from './task-list.service';
import { ITaskList, ITasks } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends TasklistService{

  constructor(http:HttpClient){
    super(http);
  }

  getTaskList():Promise<ITaskList[]>{
     return this.get('http://127.0.0.1:8000/api/task_lists/', {});
  }

  getTasks(tasklist: ITaskList): Promise<ITasks[]> {
    return this.get(`http://127.0.0.1:8000/api/task_lists/${tasklist.id}/tasks/`, {});
  }
}
