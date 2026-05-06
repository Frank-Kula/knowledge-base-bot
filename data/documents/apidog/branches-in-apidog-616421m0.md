# Branches in Apidog

Maintaining API consistency during rapid sprint development can be challenging. Apidog's sprint branch feature provides a flexible mechanism for managing API sprints, allowing teams to iteratively upgrade existing endpoints and develop new ones without disrupting other team members or affecting released endpoints.

## Use Cases

### Agile API Development

Sprint branches allow developers to design and debug endpoints in isolated branches, ensuring the main branch remains stable. This separation ensures that testing and continuous integration processes are not disrupted, maintaining the consistency of original endpoints until new versions are merged.

### Agile API Testing

Updated endpoints in sprint branches are automatically flagged within testing scenarios. Testers can quickly duplicate, adjust, and execute automated tests for endpoints within the sprint branch, ensuring that changed endpoints pass new testing tasks.

## Key Features

### Version Control

Each sprint branch functions as an independent version of the API specification, including schemas, response components, and other data.

**Benefits:**
- Data between branches does not affect each other
- Create corresponding branches for different needs
- Separate production versions from development versions
- Ensure accuracy and consistency of the main branch

### Content Protection

Sprint branches can be set as **protected**. Once protected:
- Regular content maintainers cannot edit directly
- Changes must be made in a separate sprint branch
- Modifications require a Merge Request (MR)
- Requests must be reviewed and approved by an administrator

This ensures stability and reliability of protected branches.

### Parallel Collaboration

Different team roles can work concurrently on separate branches, enhancing:
- Work efficiency
- Collaboration flexibility
- Reduced interference between team members

### Quick Merging

Once functional development in a new branch is complete:
- Developers can seamlessly merge the sprint branch back into the main branch
- New features integrate without introducing unnecessary risks
- Updates occur smoothly and safely

### Automatic Matching

The sprint branch feature automatically:
- Identifies updated endpoints in the new branch
- Marks them in relevant testing scenarios
- Enables testers to swiftly create test scenarios for new or modified endpoints
- Ensures all changes meet functional expectations

## Accessing Sprint Branches

To access a sprint branch within your project:

1. Locate the sprint branch switch next to **APIs**
2. Click to view available branches
3. Select your desired branch to switch

<Background>
![Sprint branch switch location](https://assets.apidog.com/help/assets/images/introduction-branch-01-e84c16b8a38e9d95b436d8cc0bfe72af.png)
</Background>

## Next Steps

Continue reading: [Creating a New Sprint Branch](https://docs.apidog.com/creating-a-sprint-branch-616420m0.md)

