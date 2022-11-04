import { TestBed } from '@angular/core/testing';

import { LibraryBService } from './library-b.service';

describe('LibraryBService', () => {
  let service: LibraryBService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LibraryBService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
