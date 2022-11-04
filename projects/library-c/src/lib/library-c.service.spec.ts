import { TestBed } from '@angular/core/testing';

import { LibraryCService } from './library-c.service';

describe('LibraryCService', () => {
  let service: LibraryCService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LibraryCService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
