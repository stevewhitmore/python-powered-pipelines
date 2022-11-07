import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LibraryAComponent } from './library-a.component';

describe('LibraryAComponent', () => {
  let component: LibraryAComponent;
  let fixture: ComponentFixture<LibraryAComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LibraryAComponent ],
    })
      .compileComponents();

    fixture = TestBed.createComponent(LibraryAComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
