import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LibraryDComponent } from './library-d.component';

describe('LibraryDComponent', () => {
  let component: LibraryDComponent;
  let fixture: ComponentFixture<LibraryDComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LibraryDComponent ],
    })
      .compileComponents();

    fixture = TestBed.createComponent(LibraryDComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
