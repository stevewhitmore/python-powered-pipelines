import { TestBed } from '@angular/core/testing';

import { LibraryAService } from './library-a.service';

describe('LibraryAService', () => {
  let service: LibraryAService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LibraryAService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
