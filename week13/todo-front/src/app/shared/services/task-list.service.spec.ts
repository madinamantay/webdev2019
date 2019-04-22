import { TestBed } from '@angular/core/testing';
import { TasklistService } from './task-list.service';
describe('TaskListService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));
  it('should be created', () => {
    const service: TasklistService = TestBed.get(TasklistService);
    expect(service).toBeTruthy();
  });
});
