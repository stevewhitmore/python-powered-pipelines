import { TestBed } from '@angular/core/testing';

import { LibraryDService } from './library-d.service';

describe('LibraryDService', () => {
  let service: LibraryDService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LibraryDService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
