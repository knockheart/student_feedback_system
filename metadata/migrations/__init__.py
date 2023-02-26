def create_table_data(apps, schema_editor):
    University = apps.get_model("metadata", "University")
    u = University(university_id="1", university_name="VTU")
    u.save()

    College = apps.get_model("metadata", "College")
    clg = College(college_id="1", college_name="UBDTCE", university_id=u)
    clg.save()

    Course = apps.get_model("metadata", "Course")
    c = Course(course_id="1", course_name="BE")
    c.save()

    Branch = apps.get_model("metadata", "Branch")
    b = Branch(branch_id="1", branch_name="ECE", course_id=c)
    b.save()
