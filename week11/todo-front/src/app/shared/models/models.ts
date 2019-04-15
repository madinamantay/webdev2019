export interface ITasks{
  id:number;
  name:string;
  created_at: Date;
  due_on: Date;
  status: string;
  task_list: number;
}

export interface ITaskList{
  id: number;
  name: string;
}
